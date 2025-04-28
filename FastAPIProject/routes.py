from fastapi import APIRouter
from models import Address
from config import settings

router = APIRouter()

@router.get("/", response_model=Address)
async def get_address():
    return Address(
        street="123 Main Street",
        city="Sample City",
        postcode=settings.address_postcode
    )
