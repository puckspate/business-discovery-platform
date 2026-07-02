from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: str
    discovery_id: str
    file_name: str
    file_type: str | None
    file_size: int
    storage_path: str
    status: str
    uploaded_at: datetime