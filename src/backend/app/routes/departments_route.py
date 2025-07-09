from fastapi import APIRouter, Path, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import DepartmentResponse, DepartmentCreate, DepartmentUpdate, DepartmentSearch
from ..services.department_service import (
    create_department, get_all_departments, get_department_by_id, 
    search_departments, update_department, delete_department
)
from ..db.database import get_session

router = APIRouter()

@router.post("/", response_model=DepartmentResponse)
async def create_department_route(
    department: DepartmentCreate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Create a new department."""
    return await create_department(department, session)

@router.get("/", response_model=list[DepartmentResponse])
async def get_departments_route(session: AsyncSession = Depends(get_session)):
    """Get all departments."""
    return await get_all_departments(session)

@router.get("/{department_id}", response_model=DepartmentResponse)
async def get_department_route(
    department_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Get a department by ID."""
    return await get_department_by_id(department_id, session)

@router.get("/search", response_model=list[DepartmentResponse])
async def search_departments_route(
    search: DepartmentSearch = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Search departments by various criteria."""
    return await search_departments(search, session)

@router.patch("/{department_id}", response_model=DepartmentResponse)
async def update_department_route(
    department_id: int = Path(gt=0),
    update_data: DepartmentUpdate = Body(...),
    session: AsyncSession = Depends(get_session)
):
    """Update a department."""
    return await update_department(department_id, update_data, session)

@router.delete("/{department_id}", status_code=204)
async def delete_department_route(
    department_id: int = Path(gt=0),
    session: AsyncSession = Depends(get_session)
):
    """Delete a department."""
    await delete_department(department_id, session)
    
