# main.py

from fastapi import FastAPI
from app.config import settings
from app.logging_config import configure_logging
from app.exception_handlers import global_exception_handler
import logging

# Configurar logs
configure_logging(settings.APP_ENV)

app = FastAPI(
    title="Product Price Tracker",
    description="API para seguimiento de precios",
    version="1.0.0"
)

# Agregar el manejador global de excepciones
app.add_exception_handler(Exception, global_exception_handler)

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
