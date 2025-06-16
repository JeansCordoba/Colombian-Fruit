from pydantic import BaseModel
from typing import Optional
from app.models import Department
from app.models import Region

class DepartmentBase(BaseModel):
    name: str
    region_id: int
    
class DepartmentCreate(DepartmentBase):
    
    