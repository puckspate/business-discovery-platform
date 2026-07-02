from app.database.duckdb import get_connection


class DocumentRepository:

    @staticmethod
    def create(values):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO documents
            (
                id,
                discovery_id,
                file_name,
                file_type,
                file_size,
                storage_path
            )

            VALUES (?, ?, ?, ?, ?, ?)
            """,
            values,
        )

        conn.close()