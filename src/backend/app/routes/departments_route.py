from fastapi import APIRouter, Path, Body
from ..schemas import DepartmentResponse, DepartmentCreate, DepartmentUpdate, DepartmentSearch, DepartmentDetailResponse
from ..services import DepartmentService


router = APIRouter()

@router.post("/", response_model=DepartmentResponse)
async def create_department(department: DepartmentCreate = Body(...)):
    department = DepartmentService.create_department(department)
    return department

@router.get("/", response_model=list[DepartmentResponse])
async def get_departments():  
    departments = DepartmentService.get_all_departments()
    return departments

@router.get("/detail", response_model=list[DepartmentDetailResponse])
async def get_departments_detail():
    departments = DepartmentService.get_all_departments()
    return departments

@router.get("/{department_id}", response_model=DepartmentResponse)
async def get_department(department_id: int = Path(gt=0)):
    department = DepartmentService.get_department_by_id(department_id)
    return department

@router.get("/detail/{department_id}", response_model=DepartmentDetailResponse)
async def get_department_detail(department_id: int = Path(gt=0)):
    department = DepartmentService.get_department_by_id(department_id)
    return department

@router.get("/search", response_model=list[DepartmentResponse])
async def search_departments(search: DepartmentSearch = Body(...)):
    departments = DepartmentService.search_departments(search)
    return departments

@router.get("/search/detail", response_model=list[DepartmentDetailResponse])
async def search_departments_detail(search: DepartmentSearch = Body(...)):
    departments = DepartmentService.search_departments(search)
    return departments

@router.patch("/{department_id}", response_model=DepartmentResponse)
async def update_department(department_id: int = Path(gt=0), update_data: DepartmentUpdate = Body(...)):
    department = DepartmentService.update_department(department_id, update_data)
    return department

@router.delete("/{department_id}", status_code=204)
async def delete_department(department_id: int = Path(gt=0)):
    DepartmentService.delete_department(department_id)
    
