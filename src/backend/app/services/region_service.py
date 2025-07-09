from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..models import Region
from ..utilities import Utilities
from .fruit_region_service import get_all_fruits_by_region
from typing import List, Dict, Any


def _serialize_region(region: Region) -> Dict[str, Any]:
    """Serialize region model to dictionary response."""
    return {
        "region_id": region.region_id,
        "name": region.name,
        "weather": region.weather,
        "altitude": region.altitude
    }


async def create_region(region_data, session: AsyncSession) -> Dict[str, Any]:
    """Create a new region asynchronously."""
    # Check for existing regions with same name
    existing_regions = await session.exec(select(Region)).all()
    normalized_new_name = Utilities.remove_accents(region_data.name.lower())
    
    for existing_region in existing_regions:
        if Utilities.remove_accents(existing_region.name.lower()) == normalized_new_name:
            raise HTTPException(status_code=400, detail="Region already exists")
    
    # Create new region
    new_region = Region(**region_data.model_dump())
    session.add(new_region)
    await session.commit()
    await session.refresh(new_region)
    
    return _serialize_region(new_region)


async def get_all_regions(session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all regions asynchronously."""
    regions = await session.exec(select(Region)).all()
    return [_serialize_region(region) for region in regions]


async def get_region_by_id(region_id: int, session: AsyncSession) -> Dict[str, Any]:
    """Get a region by ID asynchronously."""
    region = await session.exec(select(Region).where(Region.region_id == region_id)).first()
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return _serialize_region(region)


async def get_region_fruits(region_id: int, session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all fruits for a specific region asynchronously."""
    return await get_all_fruits_by_region(region_id, session)


async def search_regions(search_data, session: AsyncSession) -> List[Dict[str, Any]]:
    """Search regions by various criteria asynchronously."""
    query = select(Region)
    
    if search_data.region_id:
        query = query.where(Region.region_id == search_data.region_id)
    if search_data.name:
        query = query.where(Region.name.ilike(f"%{search_data.name}%"))
    if search_data.weather:
        query = query.where(Region.weather.ilike(f"%{search_data.weather}%"))
    if search_data.altitude:
        query = query.where(Region.altitude == search_data.altitude)
    
    regions = await session.exec(query).all()
    if not regions:
        raise HTTPException(status_code=404, detail="No regions found")
    
    return [_serialize_region(region) for region in regions]


async def update_region(region_id: int, update_data, session: AsyncSession) -> Dict[str, Any]:
    """Update a region asynchronously."""
    region = await session.exec(select(Region).where(Region.region_id == region_id)).first()
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    
    # Check for name conflicts
    if update_data.name:
        existing_regions = await session.exec(select(Region)).all()
        normalized_new_name = Utilities.remove_accents(update_data.name.lower())
        
        for existing_region in existing_regions:
            if (Utilities.remove_accents(existing_region.name.lower()) == normalized_new_name and
                existing_region.region_id != region_id):
                raise HTTPException(status_code=400, detail="Region already exists")
    
    # Update region
    region_data = update_data.model_dump(exclude_unset=True)
    for field, value in region_data.items():
        setattr(region, field, value)
    
    await session.commit()
    await session.refresh(region)
    
    return _serialize_region(region)


async def delete_region(region_id: int, session: AsyncSession) -> None:
    """Delete a region asynchronously."""
    region = await session.exec(select(Region).where(Region.region_id == region_id)).first()
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    
    await session.delete(region)
    await session.commit()