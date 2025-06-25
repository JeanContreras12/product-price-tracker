import logging
import os
from datetime import datetime
from app.config import settings  # Importa la configuración con APP_ENV

def configure_logging():
    """
    Configura el logging según el entorno definido en settings.APP_ENV.
    En desarrollo usa nivel DEBUG, en producción WARNING.
    """
    env = settings.APP_ENV  # Obtiene el entorno desde la configuración centralizada

    level = logging.DEBUG if env == "development" else logging.WARNING

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s - %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
    )

    log_dir = "logs"
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception as e:
        print(f"No se pudo crear el directorio de logs: {e}")

    current_date = datetime.now().strftime("%d-%m-%Y")
    log_filename = f"{log_dir}/app_{current_date}.log"

    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
