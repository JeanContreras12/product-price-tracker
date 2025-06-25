from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache

class Settings(BaseSettings):
    APP_ENV: str = Field(default="development", env="APP_ENV")
    PORT: int = Field(default=8000, env="PORT")
    DEBUG: bool = Field(default=False)
    
    # PostgreSQL
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    
    # Webhook opcional
    DISCORD_WEBHOOK_URL: str | None = Field(default=None, env="DISCORD_WEBHOOK_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "production"

    @property
    def is_development(self) -> bool:
        return self.APP_ENV == "development"

# Instancia cacheada para evitar múltiples lecturas
@lru_cache()
def get_settings():
    return Settings()

# Instancia directa si prefieres importar como antes
settings = get_settings()
