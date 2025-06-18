from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.config import settings
from app.logging_config import configure_logging
import logging

# Configurar logs
configure_logging(settings.APP_ENV)

app = FastAPI(
    title="Product Price Tracker",
    description="API para seguimiento de precios",
    version="1.0.0"
)

# Manejo global de excepciones
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger = logging.getLogger()
    logger.error(f"Excepción no controlada en {request.url}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"}
    )

@app.get("/")
def read_root():
    logger = logging.getLogger()
    logger.info("Ruta '/' accedida")
    return {
        "message": "Bienvenido al Product Price Tracker API",
        "entorno": settings.APP_ENV,
        "debug": settings.DEBUG
    }

# Ruta que genera un error a propósito (para probar)
@app.get("/error")
def trigger_error():
    raise ValueError("Esto es un error forzado para test")
