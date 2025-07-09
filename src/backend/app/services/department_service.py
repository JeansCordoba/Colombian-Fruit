from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from ..models import Department, Region
from ..utilities import Utilities
from typing import List, Dict, Any


def _serialize_department(department: Department) -> Dict[str, Any]:
    """Serialize department model to dictionary response."""
    return {
        "department_id": department.department_id,
        "name": department.name,
        "region_id": department.region_id,
        "region_name": department.region.name
    }


async def create_department(department_data, session: AsyncSession) -> Dict[str, Any]:
    """Create a new department asynchronously."""
    # Check for existing departments with same name
    existing_departments = await session.exec(select(Department)).all()
    normalized_new_name = Utilities.remove_accents(department_data.name.lower())
    
    for existing_department in existing_departments:
        if Utilities.remove_accents(existing_department.name.lower()) == normalized_new_name:
            raise HTTPException(status_code=400, detail="Department already exists")
    
    # Verify region exists
    region = await session.exec(select(Region).where(Region.region_id == department_data.region_id)).first()
    if not region:
        raise HTTPException(status_code=400, detail="Region not found")
    
    # Create new department
    new_department = Department(**department_data.model_dump())
    session.add(new_department)
    await session.commit()
    await session.refresh(new_department)
    
    return _serialize_department(new_department)


async def get_all_departments(session: AsyncSession) -> List[Dict[str, Any]]:
    """Get all departments asynchronously."""
    departments = await session.exec(select(Department)).all()
    return [_serialize_department(department) for department in departments]


async def get_department_by_id(department_id: int, session: AsyncSession) -> Dict[str, Any]:
    """Get a department by ID asynchronously."""
    department = await session.exec(select(Department).where(Department.department_id == department_id)).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    
    return _serialize_department(department)


async def search_departments(search_data, session: AsyncSession) -> List[Dict[str, Any]]:
    """Search departments by various criteria asynchronously."""
    query = select(Department)
    
    if search_data.department_id:
        query = query.where(Department.department_id == search_data.department_id)
    if search_data.name:
        normalized_name = Utilities.remove_accents(search_data.name.lower())
        query = query.where(Department.name.ilike(f"%{normalized_name}%"))
    if search_data.region_id:
        query = query.where(Department.region_id == search_data.region_id)
    if search_data.region_name:
        normalized_region_name = Utilities.remove_accents(search_data.region_name.lower())
        query = query.join(Region).where(Region.name.ilike(f"%{normalized_region_name}%"))
    
    departments = await session.exec(query).all()
    if not departments:
        raise HTTPException(status_code=404, detail="No departments found")
    
    return [_serialize_department(department) for department in departments]


async def update_department(department_id: int, update_data, session: AsyncSession) -> Dict[str, Any]:
    """Update a department asynchronously."""
    department = await session.exec(select(Department).where(Department.department_id == department_id)).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    
    # Verify region exists if updating
    if update_data.region_id:
        region = await session.exec(select(Region).where(Region.region_id == update_data.region_id)).first()
        if not region:
            raise HTTPException(status_code=400, detail="Region not found")
    
    # Check for name conflicts
    if update_data.name:
        existing_departments = await session.exec(select(Department)).all()
        normalized_new_name = Utilities.remove_accents(update_data.name.lower())
        
        for existing_department in existing_departments:
            if (Utilities.remove_accents(existing_department.name.lower()) == normalized_new_name and
                existing_department.department_id != department_id):
                raise HTTPException(status_code=400, detail="Department already exists")
    
    # Update department
    department_data = update_data.model_dump(exclude_unset=True)
    for field, value in department_data.items():
        setattr(department, field, value)
    
    await session.commit()
    await session.refresh(department)
    
    return _serialize_department(department)


async def delete_department(department_id: int, session: AsyncSession) -> None:
    """Delete a department asynchronously."""
    department = await session.exec(select(Department).where(Department.department_id == department_id)).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    
    await session.delete(department)
    await session.commit()
        