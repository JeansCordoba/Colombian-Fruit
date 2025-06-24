from ..db import get_session
from ..models import TypePlant
from ..utilities import Utilities
from fastapi import HTTPException
from sqlmodel import select


class TypePlantService:
    @staticmethod
    def _serialize_type_plant(type_plant):
        return {
            "type_plant_id": type_plant.type_plant_id,
            "name": type_plant.name
        }
    
    @staticmethod
    def create_type_plant(type_plant):
        with get_session() as session:
            existing_type_plants = session.exec(select(TypePlant)).all()
            normalized_new_name = Utilities.remove_accents(type_plant.name.lower())
            for existing_type_plant in existing_type_plants:
                if Utilities.remove_accents(existing_type_plant.name.lower()) == normalized_new_name:
                    raise HTTPException(status_code=400, detail="Type plant already exists")
            new_type_plant = TypePlant(**type_plant.model_dump())
            session.add(new_type_plant)
            session.commit()
            session.refresh(new_type_plant)
            return TypePlantService._serialize_type_plant(new_type_plant)
        
    @staticmethod
    def get_all_type_plants():
        with get_session() as session:
            type_plants = session.exec(select(TypePlant)).all()
            return [TypePlantService._serialize_type_plant(type_plant) for type_plant in type_plants]
        
    @staticmethod
    def get_type_plant_by_id(type_plant_id: int):
        with get_session() as session:
            type_plant = session.exec(select(TypePlant).where(TypePlant.type_plant_id == type_plant_id)).first()
            if not type_plant:
                raise HTTPException(status_code=404, detail="Type plant not found")
            return TypePlantService._serialize_type_plant(type_plant)
        
    @staticmethod
    def search_type_plants(search):
        with get_session() as session:
            query = select(TypePlant)
            if search.type_plant_id:
                query = query.where(TypePlant.type_plant_id == search.type_plant_id)
            if search.name:
                query = query.where(TypePlant.name.ilike(f"%{search.name}%"))
            type_plants = query.all()
            if not type_plants:
                raise HTTPException(status_code=404, detail="No type plants found")
            return [TypePlantService._serialize_type_plant(type_plant) for type_plant in type_plants]
        
    @staticmethod
    def update_type_plant(type_plant_id: int, update_data):
        with get_session() as session:
            type_plant = session.exec(select(TypePlant).where(TypePlant.type_plant_id == type_plant_id)).first()
            if not type_plant:
                raise HTTPException(status_code=404, detail="Type plant not found")
            if update_data.name:
                normalized_new_name = Utilities.remove_accents(update_data.name.lower())
                for existing_type_plant in session.exec(select(TypePlant)):
                    if Utilities.remove_accents(existing_type_plant.name.lower()) == normalized_new_name:
                        raise HTTPException(status_code=400, detail="Type plant already exists")
            type_plant_data = update_data.model_dump()
            session.exec(select(TypePlant).where(TypePlant.type_plant_id == type_plant_id)).update(type_plant_data)
            session.commit()
            session.refresh(type_plant)
            return TypePlantService._serialize_type_plant(type_plant)
        
    @staticmethod
    def delete_type_plant(type_plant_id: int):
        with get_session() as session:
            type_plant = session.exec(select(TypePlant).where(TypePlant.type_plant_id == type_plant_id)).first()
            if not type_plant:
                raise HTTPException(status_code=404, detail="Type plant not found")
            session.delete(type_plant)
            session.commit()