import sqlite3

from settings import settings


def get_db_connection():
    return sqlite3.connect(settings.DATABASE_URL)
