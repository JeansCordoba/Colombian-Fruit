from ..db import get_session
from ..models import Department, Region
from ..utilities import Utilities
from fastapi import HTTPException
from sqlmodel import select


class DepartmentService:
    @staticmethod
    def serialize_department(department):
        return {
            "department_id": department.department_id,
            "name": department.name,
            "region_id": department.region_id,
            "region_name": department.region.name
        }
    
    @staticmethod
    def create_department(department):
        with get_session() as session:
            exist_department = session.exec(select(Department)).all()
            normalized_new_name = Utilities.remove_accents(department.name.lower())
            for exist_department in exist_department:
                if Utilities.remove_accents(exist_department.name.lower()) == normalized_new_name:
                    raise HTTPException(status_code=400, detail="Department already exists")
            if not session.exec(select(Region).where(Region.region_id == department.region_id)).first():
                raise HTTPException(status_code=400, detail="Region not found")
            
            new_department = Department(**department.model_dump())
            session.add(new_department)
            session.commit()
            session.refresh(new_department)
            return DepartmentService.serialize_department(new_department)
    
    @staticmethod
    def get_all_departments():
        with get_session() as session:
            query = session.exec(select(Department)).all()
            departments = []
            for department in query:
                departments.append(DepartmentService.serialize_department(department))
            return departments
        
    @staticmethod
    def get_department_by_id(department_id: int):
        with get_session() as session:
            department = session.exec(select(Department).where(Department.department_id == department_id)).first()
            if not department:
                raise HTTPException(status_code=404, detail="Department not found")
            return DepartmentService.serialize_department(department)
        
    @staticmethod
    def search_departments(search):
        with get_session() as session:
            query = select(Department)
            if search.department_id:
                query = query.where(Department.department_id == search.department_id)
            if search.name:
                query = query.where(Department.name.ilike(f"%{search.name}%"))
            if search.region_id:
                query = query.where(Department.region_id == search.region_id)
            if search.region_name:
                query = query.join(Region).where(Region.name.ilike(f"%{search.region_name}%"))
            
            departments = session.exec(query).all()
            if not departments:
                raise HTTPException(status_code=404, detail="No departments found")
            departments_list = []
            for department in departments:
                departments_list.append(DepartmentService.serialize_department(department))
            return departments_list

    @staticmethod
    def update_department(department_id: int, update_data):
        with get_session() as session:
            department = session.exec(select(Department).where(Department.department_id == department_id)).first()
            exist_region = session.exec(select(Region).where(Region.region_id == update_data.region_id)).first()
            if not exist_region:
                raise HTTPException(status_code=404, detail="Region not found")
            if not department:
                raise HTTPException(status_code=404, detail="Department not found")
            if update_data.name:
                normalized_new_name = Utilities.remove_accents(update_data.name.lower())
                for existing_department in session.exec(select(Department)):    
                    if Utilities.remove_accents(existing_department.name.lower()) == normalized_new_name:
                        raise HTTPException(status_code=400, detail="Department already exists")
            department_data = update_data.model_dump()
            session.exec(select(Department).where(Department.department_id == department_id)).update(department_data)
            session.commit()
            session.refresh(department)
            return DepartmentService.serialize_department(department)
        
    @staticmethod
    def delete_department(department_id: int):
        with get_session() as session:
            department = session.exec(select(Department).where(Department.department_id == department_id)).first()
            if not department:
                raise HTTPException(status_code=404, detail="Department not found")
            session.delete(department)
            session.commit()

        