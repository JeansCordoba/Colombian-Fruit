from ..db import get_session
from ..models import Family, TypePlant
from ..utilities import Utilities
from fastapi import HTTPException
from sqlmodel import select

class FamilyService:
    @staticmethod
    def create_family(family):
        with get_session() as session:
            existing_families = session.exec(select(Family)).all()
            normalized_new_name = Utilities.remove_accents(family.name.lower())
            for existing_family in existing_families:
                if Utilities.remove_accents(existing_family.name.lower()) == normalized_new_name:
                    raise HTTPException(status_code=400, detail="Family already exists")
            if not session.exec(select(TypePlant).where(TypePlant.type_plant_id == family.type_plant_id)).first():
                raise HTTPException(status_code=400, detail="Type plant not found")
            new_family = Family(**family.model_dump())
            session.add(new_family)
            session.commit()
            session.refresh(new_family)
            return new_family
        
    @staticmethod
    def get_all_families():
        with get_session() as session:
            return session.exec(select(Family)).all()
        
    @staticmethod
    def get_family_by_id(family_id: int):
        with get_session() as session:
            result = session.exec(select(Family).where(Family.family_id == family_id)).first()
            if not result:
                raise HTTPException(status_code=404, detail="Family not found")
            return result
        
    @staticmethod
    def search_families(search):
        with get_session() as session:
            query = select(Family)
            if search.family_id:
                query = query.where(Family.family_id == search.family_id)
            if search.name:
                query = query.where(Family.name.ilike(f"%{search.name}%"))
            if search.type_plant_id:
                query = query.where(Family.type_plant_id == search.type_plant_id)
            families = query.all()
            if not families:
                raise HTTPException(status_code=404, detail="No families found")
            return families
        
    @staticmethod
    def update_family(family_id: int, update_data):
        with get_session() as session:
            result = session.exec(select(Family).where(Family.family_id == family_id)).first()
            if not result:
                raise HTTPException(status_code=404, detail="Family not found")
            if update_data.name:
                normalized_new_name = Utilities.remove_accents(update_data.name.lower())
                for existing_family in session.exec(select(Family)):
                    if Utilities.remove_accents(existing_family.name.lower()) == normalized_new_name:
                        raise HTTPException(status_code=400, detail="Family already exists")
            if update_data.type_plant_id:
                if not session.exec(select(TypePlant).where(TypePlant.type_plant_id == update_data.type_plant_id)).first():
                    raise HTTPException(status_code=400, detail="Type plant not found")
            family_data = update_data.model_dump()
            session.exec(select(Family).where(Family.family_id == family_id)).update(family_data)
            session.commit()
            session.refresh(result)
            return result
        
    @staticmethod
    def delete_family(family_id: int):
        with get_session() as session:
            result = session.exec(select(Family).where(Family.family_id == family_id)).first()
            if not result:
                raise HTTPException(status_code=404, detail="Family not found")
            session.delete(result)
            session.commit()