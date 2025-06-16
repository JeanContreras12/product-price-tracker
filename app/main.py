from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="Product Price Tracker",
    description="API para seguimiento de precios",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido al Product Price Tracker API",
        "entorno": settings.APP_ENV,
        "debug": settings.DEBUG
    }