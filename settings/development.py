from pathlib import Path

from .base import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class DevelopmentSettings(BaseSettings):
    NAME_ENVIRONMENT = "Development"

    DATABASE_URL = BASE_DIR / "labs.db"
    DEBUG = True
