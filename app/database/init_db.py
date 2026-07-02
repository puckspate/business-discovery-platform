from app.database.duckdb import get_connection


def initialize_database():
    conn = get_connection()

    # Companies table
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

    # Discoveries table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS discoveries (
            id VARCHAR PRIMARY KEY,
            company_id VARCHAR NOT NULL,
            name VARCHAR NOT NULL,
            description VARCHAR,
            status VARCHAR DEFAULT 'NEW',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.close()