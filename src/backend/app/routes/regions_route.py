from fastapi import APIRouter, Path, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import RegionCreate, RegionUpdate, RegionSearch, RegionResponse, FruitRegionResponse
from ..services.region_service import (
    create_region, get_all_regions, get_region_by_id, 
    get_region_fruits, search_regions, update_region, delete_region
)
from ..db.database import get_session

router = APIRouter()

@router.post("/", response_model=RegionResponse)
async def create_region_route(
    region: RegionCreate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Create a new region."""
    return await create_region(region, session)

@router.get("/", response_model=list[RegionResponse])
async def get_regions_route(session: AsyncSession = Depends(get_session)):
    """Get all regions."""
    return await get_all_regions(session)

@router.get("/{region_id}", response_model=RegionResponse)
async def get_region_route(
    region_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Get a region by ID."""
    return await get_region_by_id(region_id, session)

@router.get("/fruits/{region_id}", response_model=list[FruitRegionResponse])
async def get_region_fruits_route(
    region_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Get all fruits for a specific region."""
    return await get_region_fruits(region_id, session)

@router.get("/search", response_model=list[RegionResponse])
async def search_regions_route(
    search: RegionSearch = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Search regions by various criteria."""
    return await search_regions(search, session)

@router.patch("/{region_id}", response_model=RegionResponse)
async def update_region_route(
    region_id: int = Path(gt=0),
    update_data: RegionUpdate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Update a region."""
    return await update_region(region_id, update_data, session)

@router.delete("/{region_id}", status_code=204)
async def delete_region_route(
    region_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Delete a region."""
    await delete_region(region_id, session)