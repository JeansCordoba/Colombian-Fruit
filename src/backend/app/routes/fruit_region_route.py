from fastapi import APIRouter, Path, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import FruitRegionCreate, FruitRegionResponse
from ..services.fruit_region_service import (
    create_fruit_region, get_all_fruit_regions, delete_fruit_region
)
from ..db.database import get_session

router = APIRouter()

@router.post("/", response_model=FruitRegionResponse)
async def add_region_to_fruit_route(
    fruit_region: FruitRegionCreate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Add a region to a fruit."""
    return await create_fruit_region(fruit_region, session)

@router.get("/", response_model=list[FruitRegionResponse])
async def get_all_fruit_regions_route(session: AsyncSession = Depends(get_session)):
    """Get all fruit-region relationships."""
    return await get_all_fruit_regions(session)

@router.delete("/", status_code=204)
async def delete_fruit_region_route(
    fruit_id: int = Path(gt=0),
    region_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Delete a fruit-region relationship."""
    await delete_fruit_region(fruit_id, region_id, session) 