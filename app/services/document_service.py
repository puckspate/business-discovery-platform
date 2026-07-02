import shutil
import uuid
from pathlib import Path

from fastapi import UploadFile

from app.repositories.document_repository import DocumentRepository
from engine.analyzers.excel_analyzer import ExcelAnalyzer
from engine.classifiers.document_classifier import DocumentClassifier

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

    @staticmethod
    def analyze(document_id: str):

        document = DocumentRepository.get_by_id(document_id)

        if document is None:
            raise ValueError("Document not found")

        extension = Path(document["storage_path"]).suffix.lower()

        if extension not in [".xlsx", ".xlsm", ".xltx", ".xltm"]:
            return {
                "document_id": document["id"],
                "file_name": document["file_name"],
                "error": f"Unsupported file type: {extension}"
            }

        metadata = ExcelAnalyzer.analyze(document["storage_path"])
        first_sheet = metadata["worksheets"][0]

        classification = DocumentClassifier.classify(
            first_sheet["headers"]
        )

        metadata["classification"] = classification

        return {
            "document_id": document["id"],
            "file_name": document["file_name"],
            "file_type": document["file_type"],
            **metadata,
        }