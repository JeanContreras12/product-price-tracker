import os

# Si estás fuera de Docker, carga .env si existe
"""
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
"""

class Settings:
    def __init__(self):
        self.APP_ENV = os.getenv("APP_ENV", "development") #consulta app_env de .env, si no existe, development por defecto
        self.PORT = int(os.getenv("PORT", 8000))
        self.DEBUG = self.APP_ENV == "development"
        self.API_KEY = os.getenv("API_KEY", "default-key")  # opcional

# Instancia única para importar
settings = Settings()