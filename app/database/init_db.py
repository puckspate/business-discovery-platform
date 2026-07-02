from app.database.duckdb import get_connection


def initialize_database():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            id VARCHAR PRIMARY KEY,
            name VARCHAR,
            industry VARCHAR,
            country VARCHAR,
            state VARCHAR,
            city VARCHAR,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.close()