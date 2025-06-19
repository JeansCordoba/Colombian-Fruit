from ..db.database import get_session
from ..models import FruitRegion, Fruit, Region
from fastapi import HTTPException
from sqlmodel import select
from ..schemas.fruit_region_schema import FruitRegionResponse

class FruitRegionService:
    @staticmethod
    def create_fruit_region(fruit_region):
        with get_session() as session:
            # Verificar que la fruta existe
            fruit = session.exec(select(Fruit).where(Fruit.fruit_id == fruit_region.fruit_id)).first()
            if not fruit:
                raise HTTPException(status_code=404, detail="Fruit not found")
            
            # Verificar que la región existe
            region = session.exec(select(Region).where(Region.region_id == fruit_region.region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            
            # Verificar que la relación no existe ya
            existing_relation = session.exec(
                select(FruitRegion).where(
                    FruitRegion.fruit_id == fruit_region.fruit_id,
                    FruitRegion.region_id == fruit_region.region_id
                )
            ).first()
            
            if existing_relation:
                raise HTTPException(status_code=400, detail="Fruit-Region relationship already exists")
            
            # Crear la relación
            new_fruit_region = FruitRegion(**fruit_region.model_dump())
            session.add(new_fruit_region)
            session.commit()
            session.refresh(new_fruit_region)
            
            # Retornar respuesta con nombres
            return FruitRegionResponse(
                name=fruit.common_name,
                region=region.name
            )
    
    @staticmethod
    def get_fruit_regions_by_fruit(fruit_id: int):
        with get_session() as session:
            # Verificar que la fruta existe
            fruit = session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
            if not fruit:
                raise HTTPException(status_code=404, detail="Fruit not found")
            
            # Obtener todas las regiones de la fruta
            fruit_regions = session.exec(
                select(FruitRegion).where(FruitRegion.fruit_id == fruit_id)
            ).all()
            
            return fruit_regions
    
    @staticmethod
    def get_fruit_regions_by_region(region_id: int):
        with get_session() as session:
            # Verificar que la región existe
            region = session.exec(select(Region).where(Region.region_id == region_id)).first()
            if not region:
                raise HTTPException(status_code=404, detail="Region not found")
            
            # Obtener todas las frutas de la región
            fruit_regions = session.exec(
                select(FruitRegion).where(FruitRegion.region_id == region_id)
            ).all()
            
            return fruit_regions
    
    @staticmethod
    def delete_fruit_region(fruit_id: int, region_id: int):
        with get_session() as session:
            # Buscar la relación
            fruit_region = session.exec(
                select(FruitRegion).where(
                    FruitRegion.fruit_id == fruit_id,
                    FruitRegion.region_id == region_id
                )
            ).first()
            
            if not fruit_region:
                raise HTTPException(status_code=404, detail="Fruit-Region relationship not found")
            
            # Eliminar la relación
            session.delete(fruit_region)
            session.commit()
            return {"message": "Fruit-Region relationship deleted successfully"} 