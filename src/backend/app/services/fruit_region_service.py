from ..db.database import get_session
from ..models import FruitRegion, Fruit, Region
from fastapi import HTTPException
from sqlmodel import select


class FruitRegionService:
    @staticmethod
    def _serialize_fruit_region(data):
        with get_session() as session:
            fruit = session.exec(select(Fruit).where(Fruit.fruit_id == data.fruit_id)).first()
            region = session.exec(select(Region).where(Region.region_id == data.region_id)).first()
            return {
                "fruit_id": data.fruit_id,
                "region_id": data.region_id,
                "name_fruit": fruit.common_name,
                "name_region": region.name
            }
    
    @staticmethod
    def create_fruit_region(data):
        with get_session() as session:
            fruit = session.exec(select(Fruit).where(Fruit.fruit_id == data.fruit_id)).first()
            if not fruit:
                raise HTTPException(status_code=404, detail="Fruit not found")
            region = session.exec(select(Region).where(Region.region_id == data.region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            existing_relation = session.exec(select(FruitRegion).where(FruitRegion.fruit_id == data.fruit_id, FruitRegion.region_id == data.region_id)).first()
            if existing_relation:
                raise HTTPException(status_code=400, detail="Fruit-Region relationship already exists")
            new_fruit_region = FruitRegion(**data.model_dump())
            session.add(new_fruit_region)
            session.commit()
            session.refresh(new_fruit_region)
            return FruitRegionService._serialize_fruit_region(new_fruit_region)
        
    @staticmethod
    def get_all_fruit_regions():
        with get_session() as session:
            fruit_regions = session.exec(select(FruitRegion)).all()
            return [FruitRegionService._serialize_fruit_region(fruit_region) for fruit_region in fruit_regions]
    
    @staticmethod
    def get_all_regions_by_fruit(fruit_id: int):
        with get_session() as session:
            fruit = session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
            if not fruit:
                raise HTTPException(status_code=404, detail="Fruit not found")
            fruit_regions = session.exec(select(FruitRegion).where(FruitRegion.fruit_id == fruit_id)).all()
            return [FruitRegionService._serialize_fruit_region(fruit_region) for fruit_region in fruit_regions]
        
    @staticmethod
    def get_all_fruits_by_region(region_id: int):
        with get_session() as session:
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            fruit_regions = session.exec(select(FruitRegion).where(FruitRegion.region_id == region_id)).all()
            return [FruitRegionService._serialize_fruit_region(fruit_region) for fruit_region in fruit_regions]
    
    @staticmethod
    def delete_fruit_region(fruit_id: int, region_id: int):
        with get_session() as session:
            fruit_region = session.exec(select(FruitRegion).where(FruitRegion.fruit_id == fruit_id, FruitRegion.region_id == region_id)).first()
            if not fruit_region:
                raise HTTPException(status_code=404, detail="Fruit-Region relationship not found")
            session.delete(fruit_region)
            session.commit()