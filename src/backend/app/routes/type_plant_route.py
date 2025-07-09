from fastapi import APIRouter, Path, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import TypePlantResponse, TypePlantCreate, TypePlantUpdate, TypePlantSearch
from ..services.type_plant_service import (
    create_type_plant, get_all_type_plants, get_type_plant_by_id, 
    search_type_plants, update_type_plant, delete_type_plant
)
from ..db.database import get_session

router = APIRouter()

@router.post("/", response_model=TypePlantResponse)
async def create_type_plant_route(
    type_plant: TypePlantCreate,
    session: AsyncSession = Depends(get_session)
):
    """Create a new type plant."""
    return await create_type_plant(type_plant, session)

@router.get("/", response_model=list[TypePlantResponse])
async def get_types_plants_route(session: AsyncSession = Depends(get_session)):
    """Get all type plants."""
    return await get_all_type_plants(session)

@router.get("/{type_plant_id}", response_model=TypePlantResponse)
async def get_type_plant_route(
    type_plant_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Get a type plant by ID."""
    return await get_type_plant_by_id(type_plant_id, session)

@router.get("/search", response_model=list[TypePlantResponse])
async def search_type_plants_route(
    search: TypePlantSearch = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Search type plants by various criteria."""
    return await search_type_plants(search, session)

@router.patch("/{type_plant_id}", response_model=TypePlantResponse)
async def update_type_plant_route(
    type_plant_id: int = Path(gt=0),
    update_data: TypePlantUpdate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Update a type plant."""
    return await update_type_plant(type_plant_id, update_data, session)

@router.delete("/{type_plant_id}", status_code=204)
async def delete_type_plant_route(
    type_plant_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Delete a type plant."""
    await delete_type_plant(type_plant_id, session)