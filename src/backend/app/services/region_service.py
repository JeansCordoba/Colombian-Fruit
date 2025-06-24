from ..db import get_session
from ..models import Region
from ..utilities import Utilities
from .fruit_region_service import FruitRegionService
from fastapi import HTTPException
from sqlmodel import select

class RegionService:
    @staticmethod
    def _serialize_region(region):
        return {
            "region_id": region.region_id,
            "name": region.name,
            "weather": region.weather,
            "altitude": region.altitude
        }
        
    @staticmethod
    def create_region(region):
        with get_session() as session:
            existing_regions = session.exec(select(Region)).all()
            normalized_new_name = Utilities.remove_accents(region.name.lower())
            for existing_region in existing_regions:
                if Utilities.remove_accents(existing_region.name.lower()) == normalized_new_name:
                    raise HTTPException(status_code=400, detail="Region already exists")            
            new_region = Region(**region.model_dump())
            session.add(new_region)
            session.commit()
            session.refresh(new_region)
            return RegionService._serialize_region(new_region)
        
    @staticmethod
    def get_all_regions():
        with get_session() as session:
            regions = session.exec(select(Region)).all()
            return [RegionService._serialize_region(region) for region in regions]
        
    @staticmethod
    def get_region_by_id(region_id: int):
        with get_session() as session:
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            return RegionService._serialize_region(region)
        
    @staticmethod
    def get_region_fruits(region_id: int):
        return FruitRegionService.get_all_fruits_by_region(region_id)
        
    @staticmethod
    def search_regions(search):
        with get_session() as session:
            query = select(Region)
            if search.region_id:
                query = query.where(Region.region_id == search.region_id)
            if search.name:
                query = query.where(Region.name.ilike(f"%{search.name}%"))
            if search.weather:
                query = query.where(Region.weather.ilike(f"%{search.weather}%"))
            if search.altitude:
                query = query.where(Region.altitude == search.altitude)
            regions = query.all()
            if not regions:
                raise HTTPException(status_code=404, detail="No regions found")
            return [RegionService._serialize_region(region) for region in regions]

    @staticmethod
    def update_region(region_id: int, update_data):
        with get_session() as session:
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            if update_data.name:
                normalized_new_name = Utilities.remove_accents(update_data.name.lower())
                for existing_region in session.exec(select(Region)):
                    if Utilities.remove_accents(existing_region.name.lower()) == normalized_new_name:
                        raise HTTPException(status_code=400, detail="Region already exists")
            region_data = update_data.model_dump()
            session.exec(select(Region).where(Region.region_id == region_id)).update(region_data)
            session.commit()
            session.refresh(region)
            return RegionService._serialize_region(region)
    
    @staticmethod
    def delete_region(region_id: int):
        with get_session() as session:
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            session.delete(region)
            session.commit()