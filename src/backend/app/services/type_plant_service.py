from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..models import TypePlant
from ..utilities import Utilities
from typing import List, Dict, Any


def _serialize_type_plant(type_plant: TypePlant) -> Dict[str, Any]:
    """Serialize type plant model to dictionary response."""
    return {
        "type_plant_id": type_plant.type_plant_id,
        "name": type_plant.name
    }


async def create_type_plant(type_plant_data, session: AsyncSession) -> Dict[str, Any]:
    """Create a new type plant asynchronously."""
    # Check for existing type plants with same name
    existing_type_plants = await session.exec(select(TypePlant)).all()
    normalized_new_name = Utilities.remove_accents(type_plant_data.name.lower())
    
    for existing_type_plant in existing_type_plants:
        if Utilities.remove_accents(existing_type_plant.name.lower()) == normalized_new_name:
            raise HTTPException(status_code=400, detail="Type plant already exists")
    
    # Create new type plant
    new_type_plant = TypePlant(**type_plant_data.model_dump())
    session.add(new_type_plant)
    await session.commit()
    await session.refresh(new_type_plant)
    
    return _serialize_type_plant(new_type_plant)


async def get_all_type_plants(session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all type plants asynchronously."""
    type_plants = await session.exec(select(TypePlant)).all()
    return [_serialize_type_plant(type_plant) for type_plant in type_plants]


async def get_type_plant_by_id(type_plant_id: int, session: AsyncSession) -> Dict[str, Any]:
    """Get a type plant by ID asynchronously."""
    type_plant = await session.exec(select(TypePlant).where(TypePlant.type_plant_id == type_plant_id)).first()
    if not type_plant:
        raise HTTPException(status_code=404, detail="Type plant not found")
    return _serialize_type_plant(type_plant)


async def search_type_plants(search_data, session: AsyncSession) -> List[Dict[str, Any]]:
    """Search type plants by various criteria asynchronously."""
    query = select(TypePlant)
    
    if search_data.type_plant_id:
        query = query.where(TypePlant.type_plant_id == search_data.type_plant_id)
    if search_data.name:
        query = query.where(TypePlant.name.ilike(f"%{search_data.name}%"))
    
    type_plants = await session.exec(query).all()
    if not type_plants:
        raise HTTPException(status_code=404, detail="No type plants found")
    
    return [_serialize_type_plant(type_plant) for type_plant in type_plants]


async def update_type_plant(type_plant_id: int, update_data, session: AsyncSession) -> Dict[str, Any]:
    """Update a type plant asynchronously."""
    type_plant = await session.exec(select(TypePlant).where(TypePlant.type_plant_id == type_plant_id)).first()
    if not type_plant:
        raise HTTPException(status_code=404, detail="Type plant not found")
    
    # Check for name conflicts
    if update_data.name:
        existing_type_plants = await session.exec(select(TypePlant)).all()
        normalized_new_name = Utilities.remove_accents(update_data.name.lower())
        
        for existing_type_plant in existing_type_plants:
            if (Utilities.remove_accents(existing_type_plant.name.lower()) == normalized_new_name and
                existing_type_plant.type_plant_id != type_plant_id):
                raise HTTPException(status_code=400, detail="Type plant already exists")
    
    # Update type plant
    type_plant_data = update_data.model_dump(exclude_unset=True)
    for field, value in type_plant_data.items():
        setattr(type_plant, field, value)
    
    await session.commit()
    await session.refresh(type_plant)
    
    return _serialize_type_plant(type_plant)


async def delete_type_plant(type_plant_id: int, session: AsyncSession) -> None:
    """Delete a type plant asynchronously."""
    type_plant = await session.exec(select(TypePlant).where(TypePlant.type_plant_id == type_plant_id)).first()
    if not type_plant:
        raise HTTPException(status_code=404, detail="Type plant not found")
    
    await session.delete(type_plant)
    await session.commit()