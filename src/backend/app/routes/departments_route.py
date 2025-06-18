from fastapi import APIRouter, Path, Body
from app.schemas.department_schema import DepartmentResponse, DepartmentCreate, DepartmentUpdate, DepartmentSearch
from app.services import DepartmentService


router = APIRouter()

@router.post("/departments", response_model=DepartmentResponse)
async def create_department(department: DepartmentCreate):
    department = DepartmentService.create_department(department)
    return department

@router.get("/departments", response_model=list[DepartmentResponse])
async def get_departments():  
    departments = DepartmentService.get_all_departments()
    return departments

@router.get("/departments/{department_id}", response_model=DepartmentResponse)
async def get_department(department_id: int = Path(gt=0)):
    department = DepartmentService.get_department_by_id(department_id)
    return department

@router.get("/departments/search", response_model=list[DepartmentResponse])
async def search_departments(search: DepartmentSearch = Body(...)):
    departments = DepartmentService.get_departments(search)
    return departments

@router.patch("/departments/{department_id}", response_model=DepartmentResponse)
async def update_department(department_id: int = Path(gt=0), update_data: DepartmentUpdate = Body(...)):
    department = DepartmentService.update_department(department_id, update_data)
    return department

@router.delete("/departments/{department_id}", status_code=204)
async def delete_department(department_id: int = Path(gt=0)):
    DepartmentService.delete_department(department_id)
    
