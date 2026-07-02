import uuid

from app.repositories.company_repository import CompanyRepository


class CompanyService:

    @staticmethod
    def create(company):

        company_id = str(uuid.uuid4())

        CompanyRepository.create(
            (
                company_id,
                company.name,
                company.industry,
                company.country,
                company.state,
                company.city,
            )
        )

        return company_id

    @staticmethod
    def get_all():

        rows = CompanyRepository.get_all()

        companies = []

        for row in rows:
            companies.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "industry": row[2],
                    "country": row[3],
                    "state": row[4],
                    "city": row[5],
                    "created_at": row[6],
                }
            )

        return companies