from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..models import Family, TypePlant
from ..utilities import Utilities
from typing import List, Dict, Any


def _serialize_family(family: Family) -> Dict[str, Any]:
    """Serialize family model to dictionary response."""
    return {
        "family_id": family.family_id,
        "name": family.name,
        "type_plant_id": family.type_plant_id,
        "description": family.description
    }


async def create_family(family_data, session: AsyncSession) -> Dict[str, Any]:
    """Create a new family asynchronously."""
    # Check for existing families with same name
    existing_families = await session.exec(select(Family)).all()
    normalized_new_name = Utilities.remove_accents(family_data.name.lower())
    
    for existing_family in existing_families:
        if Utilities.remove_accents(existing_family.name.lower()) == normalized_new_name:
            raise HTTPException(status_code=400, detail="Family already exists")
    
    # Verify type plant exists
    type_plant = await session.exec(select(TypePlant).where(TypePlant.type_plant_id == family_data.type_plant_id)).first()
    if not type_plant:
        raise HTTPException(status_code=400, detail="Type plant not found")
    
    # Create new family
    new_family = Family(**family_data.model_dump())
    session.add(new_family)
    await session.commit()
    await session.refresh(new_family)
    
    return _serialize_family(new_family)


async def get_all_families(session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all families asynchronously."""
    families = await session.exec(select(Family)).all()
    return [_serialize_family(family) for family in families]


async def get_family_by_id(family_id: int, session: AsyncSession) -> Dict[str, Any]:
    """Get a family by ID asynchronously."""
    family = await session.exec(select(Family).where(Family.family_id == family_id)).first()
    if not family:
        raise HTTPException(status_code=404, detail="Family not found")
    return _serialize_family(family)


async def search_families(search_data, session: AsyncSession) -> List[Dict[str, Any]]:
    """Search families by various criteria asynchronously."""
    query = select(Family)
    
    if search_data.family_id:
        query = query.where(Family.family_id == search_data.family_id)
    if search_data.name:
        query = query.where(Family.name.ilike(f"%{search_data.name}%"))
    if search_data.type_plant_id:
        query = query.where(Family.type_plant_id == search_data.type_plant_id)
    
    families = await session.exec(query).all()
    if not families:
        raise HTTPException(status_code=404, detail="No families found")
    
    return [_serialize_family(family) for family in families]


async def update_family(family_id: int, update_data, session: AsyncSession) -> Dict[str, Any]:
    """Update a family asynchronously."""
    family = await session.exec(select(Family).where(Family.family_id == family_id)).first()
    if not family:
        raise HTTPException(status_code=404, detail="Family not found")
    
    # Check for name conflicts
    if update_data.name:
        existing_families = await session.exec(select(Family)).all()
        normalized_new_name = Utilities.remove_accents(update_data.name.lower())
        
        for existing_family in existing_families:
            if (Utilities.remove_accents(existing_family.name.lower()) == normalized_new_name and
                existing_family.family_id != family_id):
                raise HTTPException(status_code=400, detail="Family already exists")
    
    # Verify type plant exists if updating
    if update_data.type_plant_id:
        type_plant = await session.exec(select(TypePlant).where(TypePlant.type_plant_id == update_data.type_plant_id)).first()
        if not type_plant:
            raise HTTPException(status_code=400, detail="Type plant not found")
    
    # Update family
    family_data = update_data.model_dump(exclude_unset=True)
    for field, value in family_data.items():
        setattr(family, field, value)
    
    await session.commit()
    await session.refresh(family)
    
    return _serialize_family(family)


async def delete_family(family_id: int, session: AsyncSession) -> None:
    """Delete a family asynchronously."""
    family = await session.exec(select(Family).where(Family.family_id == family_id)).first()
    if not family:
        raise HTTPException(status_code=404, detail="Family not found")
    
    await session.delete(family)
    await session.commit()