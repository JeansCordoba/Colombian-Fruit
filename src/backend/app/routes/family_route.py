from fastapi import APIRouter, Path, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import FamilyCreate, FamilyUpdate, FamilySearch, FamilyResponse
from ..services.family_service import (
    create_family, get_all_families, get_family_by_id, 
    search_families, update_family, delete_family
)
from ..db.database import get_session

router = APIRouter()

@router.post("/", response_model=FamilyResponse)
async def create_family_route(
    family: FamilyCreate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Create a new family."""
    return await create_family(family, session)

@router.get("/", response_model=list[FamilyResponse])
async def get_families_route(session: AsyncSession = Depends(get_session)):
    """Get all families."""
    return await get_all_families(session)

@router.get("/{family_id}", response_model=FamilyResponse)
async def get_family_route(
    family_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Get a family by ID."""
    return await get_family_by_id(family_id, session)

@router.get("/search", response_model=list[FamilyResponse])
async def search_families_route(
    search: FamilySearch = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Search families by various criteria."""
    return await search_families(search, session)

@router.patch("/{family_id}", response_model=FamilyResponse)
async def update_family_route(
    family_id: int = Path(gt=0),
    update_data: FamilyUpdate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Update a family."""
    return await update_family(family_id, update_data, session)

@router.delete("/{family_id}", status_code=204)
async def delete_family_route(
    family_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Delete a family."""
    await delete_family(family_id, session)
