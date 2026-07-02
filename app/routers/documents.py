from fastapi import APIRouter, File, UploadFile

from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
def upload_document(
    discovery_id: str,
    file: UploadFile = File(...)
):

    document_id = DocumentService.upload(
        discovery_id,
        file,
    )

    return {
        "success": True,
        "message": "Document uploaded successfully",
        "data": {
            "id": document_id
        }
    }