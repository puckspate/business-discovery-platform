from datetime import datetime

from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    industry: str
    country: str
    state: str
    city: str


class CompanyResponse(BaseModel):
    id: str
    name: str
    industry: str
    country: str
    state: str
    city: str
    created_at: datetime