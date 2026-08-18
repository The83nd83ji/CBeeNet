# relay_vmess.py
# VMess over WebSocket (vmess-ws)
# مسیر: /vmess-ws/{uuid}

import asyncio
import secrets
import hashlib
import struct
from datetime import datetime
from Crypto.Cipher import AES
from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from main import (
    LINKS, LINKS_LOCK, stats, connections, error_logs, logger,
    is_link_allowed, save_state, log_activity, now_ir
)
from relay_vless import _ws_client_ip, check_and_use, RELAY_BUF

router = APIRouter()

def vmess_key_from_uuid(uuid: str) -> bytes:
    return hashlib.md5(uuid.encode()).digest()

def vmess_decrypt_header(key: bytes, data: bytes) -> tuple:
    if len(data) < 16:
        raise ValueError("Header too short for IV")
    iv = data[:16]
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    decrypted = cipher.decrypt(data[16:])
    if len(decrypted) < 21:
        raise ValueError("Decrypted header too short")
    version = decrypted[0]
    if version != 0x01:
        # کلاینت ممکن است نسخه‌ی دیگری ارسال کند، اما ما فقط نسخه‌ی ۱ را پشتیبانی می‌کنیم
        raise ValueError(f"Unsupported VMess version: {version}")
    
    command = decrypted[17]
    port = struct.unpack('>H', decrypted[18:20])[0]
    addr_type = decrypted[20]
    pos = 21
    if addr_type == 1:
        address = ".".join(str(b) for b in decrypted[pos:pos+4])
        pos += 4
    elif addr_type == 2:
        dlen = decrypted[pos]
        pos += 1
        address = decrypted[pos:pos+dlen].decode('utf-8', errors='ignore')
        pos += dlen
    elif addr_type == 3:
        ab = decrypted[pos:pos+16]
        pos += 16
        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"Unknown address type: {addr_type}")
    return command, address, port, decrypted[pos:]

async def relay_ws_to_tcp(ws, writer, conn_id, uuid):
    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break
            data = msg.get("bytes") or (msg.get("text") or "").encode()
            if not data:
                continue
            if not await check_and_use(uuid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            stats["total_requests"] += 1
            connections[conn_id]["bytes"] += len(data)
            writer.write(data)
            if writer.transport.get_write_buffer_size() > RELAY_BUF:
                await writer.drain()
    except (WebSocketDisconnect, Exception):
        pass
    finally:
        try:
            writer.write_eof()
        except Exception:
            pass

async def relay_tcp_to_ws(ws, reader, conn_id, uuid):
    first = True
    try:
        while True:
            data = await reader.read(RELAY_BUF)
            if not data:
                break
            if not await check_and_use(uuid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            connections[conn_id]["bytes"] += len(data)
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await ws.send_bytes(payload)
    except Exception:
        pass

@router.websocket("/vmess-ws/{uuid}")
async def vmess_standard_tunnel(ws: WebSocket, uuid: str):
    await ws.accept()

    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not is_link_allowed(link):
        logger.warning(f"VMess rejected uuid={uuid[:8]}…")
        await ws.close(code=1008, reason="not authorized")
        return

    try:
        first_msg = await asyncio.wait_for(ws.receive(), timeout=15.0)
        if first_msg["type"] == "websocket.disconnect":
            return
        first_chunk = first_msg.get("bytes") or (first_msg.get("text") or "").encode()
        if not first_chunk:
            await ws.close(code=1008, reason="empty payload")
            return
    except asyncio.TimeoutError:
        await ws.close(code=1008, reason="timeout")
        return

    key = vmess_key_from_uuid(uuid)
    try:
        command, address, port, remaining = vmess_decrypt_header(key, first_chunk)
    except Exception as e:
        logger.warning(f"VMess header decryption error: {e}")
        await ws.close(code=1008, reason="invalid vmess header")
        return

    ip = _ws_client_ip(ws)
    conn_id = secrets.token_urlsafe(6)
    connections[conn_id] = {
        "uuid": uuid,
        "ip": ip,
        "transport": "vmess-ws",
        "connected_at": datetime.now().isoformat(),
        "bytes": 0,
    }
    logger.info(f"VMess [{conn_id}] uuid={uuid[:8]}… ip={ip}")
    log_activity("connection", f"VMess از {ip} (کانفیگ {link.get('label','?')})", "info")

    writer = None
    try:
        if not await check_and_use(uuid, len(first_chunk)):
            await ws.close(code=1008, reason="quota/disabled")
            return
        stats["total_requests"] += 1
        connections[conn_id]["bytes"] += len(first_chunk)
        logger.info(f"VMess [{conn_id}] → {address}:{port}")

        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(address, port),
            timeout=10.0
        )
        sock = writer.transport.get_extra_info('socket')
        if sock:
            import socket
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        if remaining:
            writer.write(remaining)
            await writer.drain()

        done, pending = await asyncio.wait(
            {
                asyncio.create_task(relay_ws_to_tcp(ws, writer, conn_id, uuid)),
                asyncio.create_task(relay_tcp_to_ws(ws, reader, conn_id, uuid)),
            },
            return_when=asyncio.FIRST_COMPLETED,
        )
        for t in pending:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass

        asyncio.create_task(save_state())

    except WebSocketDisconnect:
        pass
    except asyncio.TimeoutError:
        stats["total_errors"] += 1
        error_logs.append({"error": "vmess connection timeout", "time": datetime.now().isoformat()})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        logger.error(f"VMess error [{conn_id}]: {exc}")
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        connections.pop(conn_id, None)
        logger.info(f"VMess closed [{conn_id}] total={len(connections)}")
