from typing import List

from fastapi import APIRouter

from app.schemas.company import CompanyCreate, CompanyResponse
from app.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("", response_model=dict)
def create_company(company: CompanyCreate):

    company_id = CompanyService.create(company)

    return {
        "id": company_id,
        "message": "Company created successfully",
    }


@router.get("", response_model=List[CompanyResponse])
def get_companies():

    return CompanyService.get_all()