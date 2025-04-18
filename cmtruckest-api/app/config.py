from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_ENV = os.getenv("APP_ENV")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")

    STORAGE_PATH = os.getenv("STORAGE_PATH")

    YOLO_API_URL = os.getenv("YOLO_API_URL")
    LLM_API_URL = os.getenv("LLM_API_URL")

settings = Settings()
