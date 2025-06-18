from app.db.database import get_session
from app.models import Region
from app.schemas.region_schema import RegionCreate, RegionUpdate, RegionSearch
from fastapi import HTTPException
from sqlmodel import select, text
import unicodedata

class RegionService:
    @staticmethod
    def remove_accents(text: str) -> str:
        # Diccionario simple de reemplazo de acentos
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'ü': 'u', 'Ü': 'U', 'ñ': 'n', 'Ñ': 'N'
        }
        for accented, unaccented in replacements.items():
            text = text.replace(accented, unaccented)
        return text

    @staticmethod
    def create_region(region):
        with get_session() as session:
            # Obtener todas las regiones
            existing_regions = session.exec(select(Region)).all()
            
            # Normalizar el nombre de la nueva región (quitar acentos y convertir a minúsculas)
            normalized_new_name = RegionService.remove_accents(region.name.lower())
            
            # Verificar si existe una región con el mismo nombre (ignorando acentos y mayúsculas)
            for existing_region in existing_regions:
                if RegionService.remove_accents(existing_region.name.lower()) == normalized_new_name:
                    raise HTTPException(
                        status_code=400, 
                        detail=f"Ya existe una región con el nombre: {existing_region.name}"
                    )
            
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
    def get_regions(search):
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
    def update_region(region_id: int, update_data):
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