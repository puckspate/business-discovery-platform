import uuid

from app.repositories.discovery_repository import DiscoveryRepository


class DiscoveryService:

    @staticmethod
    def create(discovery):

        discovery_id = str(uuid.uuid4())

        DiscoveryRepository.create(
            (
                discovery_id,
                discovery.company_id,
                discovery.name,
                discovery.description,
            )
        )

        return discovery_id

    @staticmethod
    def get_all():

        rows = DiscoveryRepository.get_all()

        discoveries = []

        for row in rows:

            discoveries.append(
                {
                    "id": row[0],
                    "company_id": row[1],
                    "name": row[2],
                    "description": row[3],
                    "status": row[4],
                    "created_at": row[5],
                }
            )

        return discoveries