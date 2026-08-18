# relay_mtproto.py
# MTProto proxy via mtg binary
import asyncio
import secrets
import subprocess
import os
from datetime import datetime
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from main import logger

router = APIRouter()

# Path to mtg binary - install with: curl -L https://github.com/9seconds/mtg/releases/latest/download/mtg -o /usr/local/bin/mtg && chmod +x /usr/local/bin/mtg
MTG_BINARY = os.environ.get("MTG_BINARY", "/usr/local/bin/mtg")
MTPROTO_SECRETS = {}

@router.post("/mtproto/start/{uuid}")
async def start_mtproto(uuid: str):
    """Start an MTProto proxy instance for a given UUID"""
    try:
        # Generate a random secret (16 bytes hex)
        secret = secrets.token_hex(16)
        port = secrets.randbelow(100) + 10200  # 10200-10299
        
        # Start mtg process
        cmd = [
            MTG_BINARY,
            "--secret", secret,
            "run",
            f"0.0.0.0:{port}"
        ]
        
        # Store the process info
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        MTPROTO_SECRETS[uuid] = {
            "port": port,
            "secret": secret,
            "process": process,
            "started_at": datetime.now().isoformat()
        }
        
        logger.info(f"MTProto started for {uuid} on port {port}")
        return {
            "ok": True,
            "port": port,
            "secret": secret,
            "link": f"tg://proxy?server={os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost')}&port={port}&secret={secret}"
        }
    except Exception as e:
        logger.error(f"Failed to start MTProto: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/mtproto/stop/{uuid}")
async def stop_mtproto(uuid: str):
    """Stop an MTProto proxy instance"""
    if uuid in MTPROTO_SECRETS:
        try:
            process = MTPROTO_SECRETS[uuid]["process"]
            process.terminate()
            await process.wait()
            del MTPROTO_SECRETS[uuid]
            return {"ok": True, "stopped": True}
        except Exception as e:
            logger.error(f"Failed to stop MTProto: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    return {"ok": True, "stopped": False}

@router.get("/mtproto/status/{uuid}")
async def mtproto_status(uuid: str):
    """Get status of an MTProto proxy instance"""
    if uuid in MTPROTO_SECRETS:
        data = MTPROTO_SECRETS[uuid]
        return {
            "running": True,
            "port": data["port"],
            "secret": data["secret"],
            "started_at": data["started_at"]
        }
    return {"running": False}
