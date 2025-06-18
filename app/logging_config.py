import logging
import os
from datetime import datetime 
def configure_logging(env: str):
    level = logging.DEBUG if env == "development" else logging.WARNING

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s - %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
    )

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
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
