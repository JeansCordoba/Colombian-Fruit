from ..db import get_session
from ..models import Fruit, Family
from ..utilities import Utilities
from .fruit_region_service import FruitRegionService
from fastapi import HTTPException
from sqlmodel import select


class FruitService:
    @staticmethod
    def _serialize_fruit(fruit):
        return {
            "fruit_id": fruit.fruit_id,
            "common_name": fruit.common_name,
            "scientific_name": fruit.scientific_name,
            "family_id": fruit.family_id,
            "season": fruit.season,
            "description": fruit.description
        }
    
    @staticmethod
    def create_fruit(fruit):
        with get_session() as session:
            existing_fruits = session.exec(select(Fruit)).all()
            normalized_new_name = Utilities.remove_accents(fruit.common_name.lower())
            normalized_new_scientific_name = Utilities.remove_accents(fruit.scientific_name.lower())
            for existing_fruit in existing_fruits:
                if Utilities.remove_accents(existing_fruit.common_name.lower()) == normalized_new_name:
                    raise HTTPException(status_code=400, detail="Common name already exists")
                if Utilities.remove_accents(existing_fruit.scientific_name.lower()) == normalized_new_scientific_name:
                    raise HTTPException(status_code=400, detail="Scientific name already exists")
            if not session.exec(select(Family).where(Family.family_id == fruit.family_id)).first():
                raise HTTPException(status_code=400, detail="Family not found")
            new_fruit = Fruit(**fruit.model_dump())
            session.add(new_fruit)
            session.commit()
            session.refresh(new_fruit)
            return FruitService._serialize_fruit(new_fruit)
    
    @staticmethod
    def get_all_fruits():
        with get_session() as session:
            fruits = session.exec(select(Fruit)).all()
            return [FruitService._serialize_fruit(fruit) for fruit in fruits]
        
    @staticmethod
    def get_fruit_by_id(fruit_id: int):
        with get_session() as session:
            if not session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first():
                raise HTTPException(status_code=404, detail="Fruit not found")
            return FruitService._serialize_fruit(session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first())
        
    @staticmethod
    def get_fruit_regions(fruit_id: int):
        return FruitRegionService.get_all_regions_by_fruit(fruit_id)
        
    @staticmethod
    def search_fruits(search):
        with get_session() as session:
            query = select(Fruit)
            if search.fruit_id:
                query = query.where(Fruit.fruit_id == search.fruit_id)
            if search.common_name:
                query = query.where(Fruit.common_name.ilike(f"%{search.common_name}%"))
            if search.scientific_name:
                query = query.where(Fruit.scientific_name.ilike(f"%{search.scientific_name}%"))
            if search.family_id:
                query = query.where(Fruit.family_id == search.family_id)
            if search.season:
                query = query.where(Fruit.season.ilike(f"%{search.season}%"))
            fruits = query.all()
            if not fruits:
                raise HTTPException(status_code=404, detail="No fruits found")
            return [FruitService._serialize_fruit(fruit) for fruit in fruits]
        
    @staticmethod
    def update_fruit(fruit_id: int, update_data):
        with get_session() as session:
            fruit = session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
            if not fruit:
                raise HTTPException(status_code=404, detail="Fruit not found")
            if update_data.family_id:
                if not session.exec(select(Family).where(Family.family_id == update_data.family_id)).first():
                    raise HTTPException(status_code=400, detail="Family not found")
            normalized_new_name = Utilities.remove_accents(update_data.common_name.lower())
            normalized_new_scientific_name = Utilities.remove_accents(update_data.scientific_name.lower())
            for existing_fruit in session.exec(select(Fruit)):
                if Utilities.remove_accents(existing_fruit.common_name.lower()) == normalized_new_name:
                    raise HTTPException(status_code=400, detail="Common name already exists")
                if Utilities.remove_accents(existing_fruit.scientific_name.lower()) == normalized_new_scientific_name:
                    raise HTTPException(status_code=400, detail="Scientific name already exists")
            fruit_data = update_data.model_dump()
            session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).update(fruit_data)
            session.commit()
            session.refresh(fruit)
            return FruitService._serialize_fruit(fruit)
        
    @staticmethod
    def delete_fruit(fruit_id: int):
        with get_session() as session:
            fruit = session.exec(select(Fruit).where(Fruit.fruit_id == fruit_id)).first()
            if not fruit:
                raise HTTPException(status_code=404, detail="Fruit not found")
            session.delete(fruit)
            session.commit()
