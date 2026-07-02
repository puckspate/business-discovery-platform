from pathlib import Path

import duckdb

from app.core.config import settings


def get_connection():
    db_path = Path(settings.DUCKDB_PATH)

    # Create the directory if it doesn't exist
    db_path.parent.mkdir(parents=True, exist_ok=True)

    return duckdb.connect(str(db_path))