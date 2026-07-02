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

    @staticmethod
    def get_by_id(document_id: str):
        conn = get_connection()

        row = conn.execute(
            """
            SELECT
                id,
                discovery_id,
                file_name,
                file_type,
                file_size,
                storage_path,
                status,
                uploaded_at
            FROM documents
            WHERE id = ?
            """,
            (document_id,),
        ).fetchone()

        conn.close()

        if row is None:
            return None

        return {
            "id": row[0],
            "discovery_id": row[1],
            "file_name": row[2],
            "file_type": row[3],
            "file_size": row[4],
            "storage_path": row[5],
            "status": row[6],
            "uploaded_at": row[7],
        }