from app.database.duckdb import get_connection


class DiscoveryRepository:

    @staticmethod
    def create(values):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO discoveries
            (id, company_id, name, description)

            VALUES (?, ?, ?, ?)
            """,
            values,
        )

        conn.close()

    @staticmethod
    def get_all():

        conn = get_connection()

        rows = conn.execute(
            """
            SELECT
                id,
                company_id,
                name,
                description,
                status,
                created_at

            FROM discoveries

            ORDER BY created_at DESC
            """
        ).fetchall()

        conn.close()

        return rows