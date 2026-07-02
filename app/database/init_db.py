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

    # Documents table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS documents (
	    id VARCHAR PRIMARY KEY,
	    discovery_id VARCHAR NOT NULL,
	    file_name VARCHAR NOT NULL,
	    file_type VARCHAR,
	    file_size BIGINT,
	    storage_path VARCHAR,
	    status VARCHAR DEFAULT 'UPLOADED',
	    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	)
    """)

    conn.close()