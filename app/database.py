from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from app.config import settings

# URL de conexión desde .env cargada por Pydantic Settings
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Crear el motor y la sesión
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Función necesaria para inyectar sesiones en dependencias
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
