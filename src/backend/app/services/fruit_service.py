from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..models import Fruit, Family
from ..utilities import Utilities
from .fruit_region_service import get_all_regions_by_fruit
from typing import List, Dict, Any


def _serialize_fruit(fruit: Fruit) -> Dict[str, Any]:
    """Serialize fruit model to dictionary response."""
    return {
        "fruit_id": fruit.fruit_id,
        "common_name": fruit.common_name,
        "scientific_name": fruit.scientific_name,
        "family_id": fruit.family_id,
        "family_name": fruit.family.name,
        "season": fruit.season,
        "description": fruit.description
    }


async def create_fruit(fruit_data, session: AsyncSession) -> Dict[str, Any]:
    """Create a new fruit asynchronously."""
    # Check for existing fruits with same names
    existing_fruits = await session.exec(select(Fruit)).all()
    normalized_new_name = Utilities.remove_accents(fruit_data.common_name.lower())
    normalized_new_scientific_name = Utilities.remove_accents(fruit_data.scientific_name.lower())
    
    for existing_fruit in existing_fruits:
        if Utilities.remove_accents(existing_fruit.common_name.lower()) == normalized_new_name:
            raise HTTPException(status_code=400, detail="Common name already exists")
        if Utilities.remove_accents(existing_fruit.scientific_name.lower()) == normalized_new_scientific_name:
            raise HTTPException(status_code=400, detail="Scientific name already exists")
    
    # Verify family exists
    family = await session.exec(select(Family).where(Family.family_id == fruit_data.family_id)).first()
    if not family:
        raise HTTPException(status_code=400, detail="Family not found")
    
    # Create new fruit
    new_fruit = Fruit(**fruit_data.model_dump())
    session.add(new_fruit)
    await session.commit()
    await session.refresh(new_fruit)
    
    return _serialize_fruit(new_fruit)


async def get_all_fruits(session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all fruits asynchronously."""
    fruits = await session.exec(select(Fruit)).all()
    return [_serialize_fruit(fruit) for fruit in fruits]


async def get_fruit_by_id(fruit_id: int, session: AsyncSession) -> Dict[str, Any]:
    """Get a fruit by ID asynchronously."""
    fruit = await session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return _serialize_fruit(fruit)


async def get_fruit_regions(fruit_id: int, session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all regions for a specific fruit asynchronously."""
    return await get_all_regions_by_fruit(fruit_id, session)


async def search_fruits(search_data, session: AsyncSession) -> List[Dict[str, Any]]:
    """Search fruits by various criteria asynchronously."""
    query = select(Fruit)
    
    if search_data.fruit_id:
        query = query.where(Fruit.fruit_id == search_data.fruit_id)
    if search_data.common_name:
        query = query.where(Fruit.common_name.ilike(f"%{search_data.common_name}%"))
    if search_data.scientific_name:
        query = query.where(Fruit.scientific_name.ilike(f"%{search_data.scientific_name}%"))
    if search_data.family_id:
        query = query.where(Fruit.family_id == search_data.family_id)
    if search_data.season:
        query = query.where(Fruit.season.ilike(f"%{search_data.season}%"))
    
    fruits = await session.exec(query).all()
    if not fruits:
        raise HTTPException(status_code=404, detail="No fruits found")
    
    return [_serialize_fruit(fruit) for fruit in fruits]


async def update_fruit(fruit_id: int, update_data, session: AsyncSession) -> Dict[str, Any]:
    """Update a fruit asynchronously."""
    fruit = await session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    # Verify family exists if updating family_id
    if update_data.family_id:
        family = await session.exec(select(Family).where(Family.family_id == update_data.family_id)).first()
        if not family:
            raise HTTPException(status_code=400, detail="Family not found")
    
    # Check for name conflicts
    if update_data.common_name or update_data.scientific_name:
        existing_fruits = await session.exec(select(Fruit)).all()
        normalized_new_name = Utilities.remove_accents(update_data.common_name.lower()) if update_data.common_name else None
        normalized_new_scientific_name = Utilities.remove_accents(update_data.scientific_name.lower()) if update_data.scientific_name else None
        
        for existing_fruit in existing_fruits:
            if (normalized_new_name and 
                Utilities.remove_accents(existing_fruit.common_name.lower()) == normalized_new_name and
                existing_fruit.fruit_id != fruit_id):
                raise HTTPException(status_code=400, detail="Common name already exists")
            if (normalized_new_scientific_name and 
                Utilities.remove_accents(existing_fruit.scientific_name.lower()) == normalized_new_scientific_name and
                existing_fruit.fruit_id != fruit_id):
                raise HTTPException(status_code=400, detail="Scientific name already exists")
    
    # Update fruit
    fruit_data = update_data.model_dump(exclude_unset=True)
    for field, value in fruit_data.items():
        setattr(fruit, field, value)
    
    await session.commit()
    await session.refresh(fruit)
    
    return _serialize_fruit(fruit)


async def delete_fruit(fruit_id: int, session: AsyncSession) -> None:
    """Delete a fruit asynchronously."""
    fruit = await session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    await session.delete(fruit)
    await session.commit()
