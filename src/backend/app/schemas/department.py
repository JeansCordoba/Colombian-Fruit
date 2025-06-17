from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class DepartmentBase(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    region_id: int = Field(gt=0)
    
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "example": {
                "name": "Chocó",
                "region_id": 2
            }
        }
    }

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")
    
class DepartmentCreate(DepartmentBase):
    pass

class DepartmentRead(DepartmentBase):
    department_id: int = Field(gt=0)

class DepartmentSearch(OptionalField):
    department_id: Optional[int] = Field(gt=0)
    name: Optional[str] = Field(min_length=3, max_length=50)
    region_id: Optional[int] = Field(gt=0)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "department_id": 1,
                "name": "Chocó",
                "region_id": 2
            }
        }
    }

class DepartmentUpdate(OptionalField):
    name: Optional[str] = Field(min_length=3, max_length=50)
    region_id: Optional[int] = Field(gt=0)
    

