from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..models import FruitRegion, Fruit, Region
from typing import List, Dict, Any


async def _serialize_fruit_region(data: FruitRegion, session: AsyncSession) -> Dict[str, Any]:
    """Serialize fruit region model to dictionary response."""
    fruit = await session.exec(select(Fruit).where(Fruit.fruit_id == data.fruit_id)).first()
    region = await session.exec(select(Region).where(Region.region_id == data.region_id)).first()
    return {
        "fruit_id": data.fruit_id,
        "region_id": data.region_id,
        "fruit_name": fruit.common_name,
        "region_name": region.name
    }


async def create_fruit_region(data, session: AsyncSession) -> Dict[str, Any]:
    """Create a new fruit-region relationship asynchronously."""
    # Verify fruit exists
    fruit = await session.exec(select(Fruit).where(Fruit.fruit_id == data.fruit_id)).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    # Verify region exists
    region = await session.exec(select(Region).where(Region.region_id == data.region_id)).first()
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    
    # Check for existing relationship
    existing_relation = await session.exec(
        select(FruitRegion).where(
            FruitRegion.fruit_id == data.fruit_id, 
            FruitRegion.region_id == data.region_id
        )
    ).first()
    if existing_relation:
        raise HTTPException(status_code=400, detail="Fruit-Region relationship already exists")
    
    # Create new relationship
    new_fruit_region = FruitRegion(**data.model_dump())
    session.add(new_fruit_region)
    await session.commit()
    await session.refresh(new_fruit_region)
    
    return await _serialize_fruit_region(new_fruit_region, session)


async def get_all_fruit_regions(session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all fruit-region relationships asynchronously."""
    fruit_regions = await session.exec(select(FruitRegion)).all()
    return [await _serialize_fruit_region(fruit_region, session) for fruit_region in fruit_regions]


async def get_all_regions_by_fruit(fruit_id: int, session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all regions for a specific fruit asynchronously."""
    # Verify fruit exists
    fruit = await session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
    fruit_regions = await session.exec(select(FruitRegion).where(FruitRegion.fruit_id == fruit_id)).all()
    return [await _serialize_fruit_region(fruit_region, session) for fruit_region in fruit_regions]


async def get_all_fruits_by_region(region_id: int, session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all fruits for a specific region asynchronously."""
    # Verify region exists
    region = await session.exec(select(Region).where(Region.region_id == region_id)).first()
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    
    fruit_regions = await session.exec(select(FruitRegion).where(FruitRegion.region_id == region_id)).all()
    return [await _serialize_fruit_region(fruit_region, session) for fruit_region in fruit_regions]


async def delete_fruit_region(fruit_id: int, region_id: int, session: AsyncSession) -> None:
    """Delete a fruit-region relationship asynchronously."""
    fruit_region = await session.exec(
        select(FruitRegion).where(
            FruitRegion.fruit_id == fruit_id, 
            FruitRegion.region_id == region_id
        )
    ).first()
    if not fruit_region:
        raise HTTPException(status_code=404, detail="Fruit-Region relationship not found")
    
    await session.delete(fruit_region)
    await session.commit()