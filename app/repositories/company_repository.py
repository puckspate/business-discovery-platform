from app.database.duckdb import get_connection


class CompanyRepository:

    @staticmethod
    def create(values):
        conn = get_connection()

        conn.execute(
            """
            INSERT INTO companies
            (id, name, industry, country, state, city)
            VALUES (?, ?, ?, ?, ?, ?)
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
                name,
                industry,
                country,
                state,
                city,
                created_at
            FROM companies
            ORDER BY created_at DESC
            """
        ).fetchall()

        conn.close()

        return rows