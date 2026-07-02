import shutil
import uuid
from pathlib import Path

from fastapi import UploadFile

from app.repositories.document_repository import DocumentRepository

UPLOAD_DIR = Path("data/uploads")


class DocumentService:

    @staticmethod
    def upload(discovery_id: str, file: UploadFile):

        document_id = str(uuid.uuid4())

        discovery_folder = UPLOAD_DIR / discovery_id
        discovery_folder.mkdir(parents=True, exist_ok=True)

        destination = discovery_folder / file.filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        DocumentRepository.create(
            (
                document_id,
                discovery_id,
                file.filename,
                file.content_type,
                destination.stat().st_size,
                str(destination),
            )
        )

        return document_id