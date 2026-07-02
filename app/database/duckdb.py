import duckdb
from app.core.config import settings


def get_connection():
    return duckdb.connect(settings.DUCKDB_PATH)