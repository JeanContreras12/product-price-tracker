
from fastapi import Request
from fastapi.responses import JSONResponse
import logging, os, httpx

async def global_exception_handler(request: Request, exc: Exception):
    logger = logging.getLogger()
    logger.error(f"Excepción no controlada en {request.url}: {exc}", exc_info=True)

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook_url:
        try:
            async with httpx.AsyncClient() as client:
                await client.post(webhook_url, json={
                    "content": f"Error crítico en {request.url}\n{type(exc).__name__}: {exc}"
                })
        except Exception as e:
            logger.warning(f"No se pudo enviar la notificación a Discord: {e}")

    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"}
    )