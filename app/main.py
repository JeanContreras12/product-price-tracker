from fastapi import FastAPI
from app.config import settings
from app.logging_config import configure_logging
from app.exception_handlers import global_exception_handler
import logging
from app.database import engine
from app.models import Base
from app.routers.products import router_products
from app.routers.scraper import router_scraper

# Configurar logs
configure_logging()

# Crear las tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Price Tracker",
    description="API para seguimiento de precios",
    version="1.0.0"
)

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

@app.get("/error")
def trigger_error():
    raise ValueError("Esto es un error forzado para test")

# Incluye correctamente ambos routers
app.include_router(router_products)
app.include_router(router_scraper)

print("✅ products.py se ha importado correctamente")
