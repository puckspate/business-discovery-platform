from datetime import datetime

from pydantic import BaseModel


class DiscoveryCreate(BaseModel):
    company_id: str
    name: str
    description: str


class DiscoveryResponse(BaseModel):
    id: str
    company_id: str
    name: str
    description: str
    status: str
    created_at: datetime