from fastapi import APIRouter, Path, Body
from app.schemas.department import DepartmentRead, DepartmentCreate, DepartmentUpdate, DepartmentSearch
from app.services import DepartmentService


router = APIRouter()

@router.post("/departments", response_model=DepartmentRead)
def create_department(department: DepartmentCreate):
    department = DepartmentService.create_department(department)
    return department

@router.get("/departments", response_model=list[DepartmentRead])
def get_departments():  
    departments = DepartmentService.get_all_departments()
    return departments

@router.get("/departments/{department_id}", response_model=DepartmentRead)
def get_department(department_id: int = Path(gt=0)):
    department = DepartmentService.get_department_by_id(department_id)
    return department

@router.get("/departments/search", response_model=list[DepartmentRead])
def search_departments(search: DepartmentSearch = Body(...)):
    departments = DepartmentService.get_departments(search)
    return departments

@router.patch("/departments/{department_id}", response_model=DepartmentRead)
def update_department(department_id: int = Path(gt=0), update_data: DepartmentUpdate = Body(...)):
    department = DepartmentService.update_department(department_id, update_data)
    return department

@router.delete("/departments/{department_id}", status_code=204)
def delete_department(department_id: int = Path(gt=0)):
    return DepartmentService.delete_department(department_id)
    
    
