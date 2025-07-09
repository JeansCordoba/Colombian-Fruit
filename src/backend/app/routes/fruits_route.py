from fastapi import APIRouter, Path, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import FruitCreate, FruitResponse, FruitSearch, FruitUpdate, FruitRegionResponse
from ..services.fruit_service import (
    create_fruit, get_all_fruits, get_fruit_by_id, 
    get_fruit_regions, search_fruits, update_fruit, delete_fruit
)
from ..db.database import get_session

router = APIRouter()

@router.post("/", response_model=FruitResponse)
async def create_fruit_route(
    fruit: FruitCreate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Create a new fruit."""
    return await create_fruit(fruit, session)

@router.get("/", response_model=list[FruitResponse])
async def get_fruits_route(session: AsyncSession = Depends(get_session)):
    """Get all fruits."""
    return await get_all_fruits(session)

@router.get("/{fruit_id}", response_model=FruitResponse)
async def get_fruit_route(
    fruit_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Get a fruit by ID."""
    return await get_fruit_by_id(fruit_id, session)

@router.get("/regions/{fruit_id}", response_model=list[FruitRegionResponse])
async def get_fruit_regions_route(
    fruit_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Get all regions for a specific fruit."""
    return await get_fruit_regions(fruit_id, session)

@router.get("/search", response_model=list[FruitResponse])
async def search_fruits_route(
    search: FruitSearch = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Search fruits by various criteria."""
    return await search_fruits(search, session)

@router.patch("/{fruit_id}", response_model=FruitResponse)
async def update_fruit_route(
    fruit_id: int = Path(gt=0),
    update_data: FruitUpdate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Update a fruit."""
    return await update_fruit(fruit_id, update_data, session)

@router.delete("/{fruit_id}", status_code=204)
async def delete_fruit_route(
    fruit_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Delete a fruit."""
    await delete_fruit(fruit_id, session)
