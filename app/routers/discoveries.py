from fastapi import APIRouter

from app.schemas.discovery import DiscoveryCreate
from app.services.discovery_service import DiscoveryService

router = APIRouter(
    prefix="/discoveries",
    tags=["Discoveries"],
)


@router.post("")
def create_discovery(discovery: DiscoveryCreate):

    discovery_id = DiscoveryService.create(discovery)

    return {
        "success": True,
        "message": "Discovery created successfully",
        "data": {
            "id": discovery_id,
        },
    }


@router.get("")
def get_discoveries():

    discoveries = DiscoveryService.get_all()

    return {
        "success": True,
        "message": "Discoveries retrieved successfully",
        "count": len(discoveries),
        "data": discoveries,
    }