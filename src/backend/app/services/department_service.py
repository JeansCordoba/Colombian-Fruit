from app.db.database import get_session
from app.models import Department, Region
from fastapi import HTTPException
from sqlmodel import select
from .region_service import RegionService

class DepartmentService:
    def create_department(department):
        with get_session() as session:
            # Obtener todos los departamentos
            exist_department = session.exec(select(Department)).all()
            normalized_new_name = RegionService.remove_accents(department.name.lower())
            # Verificar si el departamento existe
            for exist_department in exist_department:
                if RegionService.remove_accents(exist_department.name.lower()) == normalized_new_name:
                    raise HTTPException(status_code=400, detail="Department already exists")
            # Verificar si la región existe
            RegionService.get_region_by_id(department.region_id)
            
            new_department = Department(**department.model_dump())
            session.add(new_department)
            session.commit()
            session.refresh(new_department)
            return new_department
    
    def get_all_departments():
        with get_session() as session:
            departments = session.exec(select(Department)).all()
            return departments
        
    def get_department_by_id(department_id: int):
        with get_session() as session:
            department = session.exec(select(Department).where(Department.department_id == department_id)).first()
            if not department:
                raise HTTPException(status_code=404, detail="Department not found")
            return department
        
    def get_departments(search):
        with get_session() as session:
            query = select(Department)
            if search.department_id:
                query = query.where(Department.department_id == search.department_id)
            if search.name:
                query = query.where(Department.name.ilike(f"%{search.name}%"))
            if search.region_id:
                query = query.where(Department.region_id == search.region_id)
            departments = query.all()
            if not departments:
                raise HTTPException(status_code=404, detail="No departments found")
            return departments

    def update_department(department_id: int, update_data):
        with get_session() as session:
            department = session.exec(select(Department).where(Department.department_id == department_id)).first()
            exist_region = session.exec(select(Region).where(Region.region_id == update_data.region_id)).first()
            if not exist_region:
                raise HTTPException(status_code=404, detail="Region not found")
            if not department:
                raise HTTPException(status_code=404, detail="Department not found")
            department_data = update_data.model_dump()
            session.exec(select(Department).where(Department.department_id == department_id)).update(department_data)
            session.commit()
            session.refresh(department)
            return department
        
    def delete_department(department_id: int):
        with get_session() as session:
            department = session.exec(select(Department).where(Department.department_id == department_id)).first()
            if not department:
                raise HTTPException(status_code=404, detail="Department not found")
            session.delete(department)
            session.commit()

        