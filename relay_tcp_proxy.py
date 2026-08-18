# relay_tcp_proxy.py
# TCP proxy with blacklist/whitelist support
import asyncio
from main import stats, hourly_traffic, error_logs, logger, now_ir, fmt_bytes

async def handle_tcp_proxy(target_url: str, request, http_client, blacklist, whitelist):
    """Handle TCP proxy requests with blacklist/whitelist filtering"""
    from fastapi import HTTPException
    from fastapi.responses import Response
    
    # Check if target is blacklisted
    if target_url in blacklist:
        logger.warning(f"TCP proxy blocked: {target_url} (blacklisted)")
        raise HTTPException(status_code=403, detail="Target is blacklisted")
    
    # Check whitelist (if whitelist is not empty, only allow whitelisted targets)
    if whitelist and target_url not in whitelist:
        logger.warning(f"TCP proxy blocked: {target_url} (not whitelisted)")
        raise HTTPException(status_code=403, detail="Target is not whitelisted")
    
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
    
    try:
        body = await request.body()
        headers = {k: v for k, v in request.headers.items() 
                   if k.lower() not in {"connection", "keep-alive", "proxy-authenticate", 
                                        "proxy-authorization", "te", "trailers", 
                                        "transfer-encoding", "upgrade", "content-encoding", 
                                        "content-length", "host"}}
        
        resp = await http_client.request(
            method=request.method,
            url=target_url,
            headers=headers,
            content=body
        )
        
        stats["total_bytes"] += len(resp.content)
        stats["total_requests"] += 1
        hourly_traffic[now_ir().strftime("%H:00")] += len(resp.content)
        
        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers={k: v for k, v in resp.headers.items() 
                     if k.lower() not in {"connection", "keep-alive", "proxy-authenticate",
                                          "proxy-authorization", "te", "trailers",
                                          "transfer-encoding", "upgrade", "content-encoding",
                                          "content-length"}}
        )
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "url": target_url, "time": now_ir().isoformat()})
        raise HTTPException(status_code=502, detail=f"TCP proxy error: {exc}")
