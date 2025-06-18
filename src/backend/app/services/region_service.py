from app.db.database import get_session
from app.models import Region
from app.schemas.region_schema import RegionCreate, RegionUpdate, RegionSearch
from fastapi import HTTPException
from sqlmodel import select

class RegionService:
    @staticmethod
    def create_region(region: RegionCreate):
        with get_session() as session:
            # Verificar si ya existe una región con el mismo nombre
            existing_region = session.exec(select(Region).where(Region.name == region.name)).first()
            if existing_region:
                raise HTTPException(status_code=400, detail="Region already exists")
            
            new_region = Region(**region.model_dump())
            session.add(new_region)
            session.commit()
            session.refresh(new_region)
            return new_region
        
    @staticmethod
    def get_all_regions():
        with get_session() as session:
            regions = session.exec(select(Region)).all()
            return regions
        
    @staticmethod
    def get_region_by_id(region_id: int):
        with get_session() as session:
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            return region
        
    @staticmethod
    def get_regions(search: RegionSearch):
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
            regions = session.exec(query).all()
            if not regions:
                raise HTTPException(status_code=404, detail="No regions found")
            return regions

    @staticmethod
    def update_region(region_id: int, update_data: RegionUpdate):
        with get_session() as session:
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            
            session.exec(select(Region).where(Region.region_id == region_id)).update(update_data.model_dump(exclude_unset=True))
            session.commit()
            session.refresh(region)
            return region
    
    @staticmethod
    def delete_region(region_id: int):
        with get_session() as session:
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            session.delete(region)
            session.commit()