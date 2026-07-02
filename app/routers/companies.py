from typing import List

from fastapi import APIRouter

from app.schemas.company import CompanyCreate, CompanyResponse
from app.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("", response_model=dict)
def create_company(company: CompanyCreate):

    company_id = CompanyService.create(company)

    return {
        "success": True,
        "message": "Company created successfully",
        "data": {
            "id": company_id
        }
    }


@router.get("", response_model=dict)
def get_companies():

    companies = CompanyService.get_all()

    return {
        "success": True,
        "message": "Companies retrieved successfully",
        "count": len(companies),
        "data": companies,
    }