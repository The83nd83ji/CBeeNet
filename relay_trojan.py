# relay_trojan.py
import asyncio
import secrets
from datetime import datetime
from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from main import (
    LINKS, LINKS_LOCK, stats, connections, error_logs, logger,
    is_link_allowed, save_state, log_activity, now_ir
)
from relay_vless import _ws_client_ip, check_and_use, RELAY_BUF

router = APIRouter()


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
                await ws.close(code=1008, reason="quota/disabled")
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
    try:
        while True:
            data = await reader.read(RELAY_BUF)
            if not data:
                break
            if not await check_and_use(uuid, len(data)):
                await ws.close(code=1008, reason="quota/disabled")
                break
            connections[conn_id]["bytes"] += len(data)
            await ws.send_bytes(data)
    except Exception:
        pass


@router.websocket("/CBeeNet-----CBeeNet-----CBeeNet-----CBeeNet-----CBeeNet-----CBeeNet-----CBeeNet-----CBeeNet-----CBeeNet-----CBeeNet/{uuid}")
async def trojan_tunnel(ws: WebSocket, uuid: str):
    await ws.accept()

    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not is_link_allowed(link):
        logger.warning(f"Trojan rejected uuid={uuid[:8]}…")
        await ws.close(code=1008, reason="not authorized")
        return

    ip = _ws_client_ip(ws)
    conn_id = secrets.token_urlsafe(6)
    connections[conn_id] = {
        "uuid": uuid,
        "ip": ip,
        "transport": "trojan-ws",
        "connected_at": datetime.now().isoformat(),
        "bytes": 0,
    }
    logger.info(f"Trojan [{conn_id}] uuid={uuid[:8]}… ip={ip}")
    log_activity("connection", f"Trojan از {ip} (کانفیگ {link.get('label','?')})", "info")

    writer = None
    try:
        # اولین پیام رو بگیر (ممکنه هدر باشه یا نباشه)
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

        # اگر هدر تروجان بود parse کن، وگرنه فقط به عنوان payload به مقصد برو
        # مقصد رو از کانفیگ نمی‌تونیم بگیریم، پس از هدر یا fallback
        address = "127.0.0.1"
        port = 443
        payload = first_chunk
        
        # سعی کن هدر رو parse کنی
        try:
            if len(first_chunk) >= 61 and first_chunk[0] == 0x01:
                # هدر تروجان معتبر
                password_bytes = first_chunk[1:57]
                null_pos = password_bytes.find(b'\x00')
                if null_pos > 0:
                    password = password_bytes[:null_pos].decode('utf-8', errors='ignore')
                else:
                    password = password_bytes.decode('utf-8', errors='ignore')
                if password == "CBeeNet":
                    pos = 57
                    command = first_chunk[pos]; pos += 1
                    port = int.from_bytes(first_chunk[pos:pos+2], "big"); pos += 2
                    addr_type = first_chunk[pos]; pos += 1
                    if addr_type == 1:
                        address = ".".join(str(b) for b in first_chunk[pos:pos+4])
                        pos += 4
                    elif addr_type == 2:
                        dlen = first_chunk[pos]; pos += 1
                        address = first_chunk[pos:pos+dlen].decode("utf-8", errors="ignore")
                        pos += dlen
                    elif addr_type == 3:
                        ab = first_chunk[pos:pos+16]
                        pos += 16
                        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
                    payload = first_chunk[pos:]
                    logger.info(f"Trojan parsed: {address}:{port}")
        except Exception as e:
            logger.warning(f"Trojan header parse failed: {e}, using fallback")

        if not await check_and_use(uuid, len(first_chunk)):
            await ws.close(code=1008, reason="quota/disabled")
            return
        stats["total_requests"] += 1
        connections[conn_id]["bytes"] += len(first_chunk)
        logger.info(f"Trojan [{conn_id}] → {address}:{port}")

        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(address, port),
            timeout=10.0
        )
        sock = writer.transport.get_extra_info('socket')
        if sock:
            import socket
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        if payload:
            writer.write(payload)
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
        error_logs.append({"error": "trojan connection timeout", "time": datetime.now().isoformat()})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        logger.error(f"Trojan error [{conn_id}]: {exc}")
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        connections.pop(conn_id, None)
        logger.info(f"Trojan closed [{conn_id}] total={len(connections)}")
