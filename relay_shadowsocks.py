# relay_shadowsocks.py
# Shadowsocks (AEAD aes-256-gcm) relay for CBeeNet Gateway
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

# Shadowsocks AEAD implementation (simplified - for production use a proper lib)
# This is a placeholder that routes traffic through a WebSocket tunnel
# For real Shadowsocks, you'd use a library like shadowsocks-libev

@router.websocket("/ss/{uuid}")
async def shadowsocks_tunnel(ws: WebSocket, uuid: str):
    await ws.accept()

    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not is_link_allowed(link):
        logger.warning(f"Shadowsocks rejected uuid={uuid[:8]}…")
        await ws.close(code=1008, reason="not authorized")
        return

    ip = _ws_client_ip(ws)
    conn_id = secrets.token_urlsafe(6)
    connections[conn_id] = {
        "uuid": uuid,
        "ip": ip,
        "transport": "shadowsocks",
        "connected_at": datetime.now().isoformat(),
        "bytes": 0,
    }
    logger.info(f"Shadowsocks [{conn_id}] uuid={uuid[:8]}… ip={ip}")
    log_activity("connection", f"Shadowsocks از {ip} (کانفیگ {link.get('label','?')})", "info")

    writer = None
    try:
        # Receive the first packet (contains address and port)
        first_msg = await asyncio.wait_for(ws.receive(), timeout=15.0)
        if first_msg["type"] == "websocket.disconnect":
            return
        data = first_msg.get("bytes") or (first_msg.get("text") or "").encode()
        if not data:
            await ws.close(code=1008, reason="empty payload")
            return

        # Parse SOCKS5-like address from Shadowsocks client
        # Format: [addr_type][address][port][payload]
        if len(data) < 4:
            await ws.close(code=1008, reason="invalid header")
            return
        
        addr_type = data[0]
        pos = 1
        if addr_type == 1:  # IPv4
            address = ".".join(str(b) for b in data[pos:pos+4])
            pos += 4
        elif addr_type == 3:  # Domain
            dlen = data[pos]
            pos += 1
            address = data[pos:pos+dlen].decode('utf-8', errors='ignore')
            pos += dlen
        else:
            await ws.close(code=1008, reason="unsupported address type")
            return
        
        if len(data) < pos + 2:
            await ws.close(code=1008, reason="invalid port")
            return
        port = int.from_bytes(data[pos:pos+2], "big")
        pos += 2
        payload = data[pos:]

        if not await check_and_use(uuid, len(data)):
            await ws.close(code=1008, reason="quota/disabled")
            return
        stats["total_requests"] += 1
        connections[conn_id]["bytes"] += len(data)
        logger.info(f"Shadowsocks [{conn_id}] → {address}:{port}")

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

        # Relay bidirectional
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
        error_logs.append({"error": "shadowsocks connection timeout", "time": datetime.now().isoformat()})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        logger.error(f"Shadowsocks error [{conn_id}]: {exc}")
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        connections.pop(conn_id, None)
        logger.info(f"Shadowsocks closed [{conn_id}] total={len(connections)}")
