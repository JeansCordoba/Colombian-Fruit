from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")
        
    model_config = {
        "extra": "ignore",
    }

class DepartmentBase(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the department")
    region_id: int = Field(gt=0, description="ID of the region of the department")
    
    model_config = {
        "extra": "forbid",
    }

class DepartmentCreate(DepartmentBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "summary": "Create a department",
                "description": "Create a department with the following data",
                    "value": {
                        "name": "Chocó",
                        "region_id": 2
                    }
                }
            ]
        }
    }

class DepartmentResponse(DepartmentBase):
    department_id: int = Field(gt=0)
    region_name: str = Field(min_length=3, max_length=50, description="Name of the region")
    
    model_config = {
        "extra": "ignore",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Department data",
                    "description": "Returns the data of a department",
                    "value": {
                        "department_id": 1,
                        "name": "Chocó",
                        "region_id": 2,
                        "region_name": "Pacífico"
                    }
                }
            ]
        }
    }


class DepartmentSearch(OptionalField):
    department_id: Optional[int] = Field(gt=0)
    name: Optional[str] = Field(min_length=3, max_length=50)
    region_id: Optional[int] = Field(gt=0)
    region_name: Optional[str] = Field(min_length=3, max_length=50)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Search by department_id",
                    "description": "Search a department by its ID",
                    "value": {
                        "department_id": 1
                    }
                },
                {
                    "summary": "Search by name",
                    "description": "Search a department by its name",
                    "value": {
                        "name": "Chocó"
                    }
                },
                {
                    "summary": "Search by region_id",
                    "description": "Search a department by its region ID",
                    "value": {
                        "region_id": 2
                    }
                },
                {
                    "summary": "Search by region name",
                    "description": "Search a department by the name of the region",
                    "value": {
                        "region_name": "Pacífico"
                    }
                }
            ]
        }
    }

class DepartmentUpdate(OptionalField):
    name: Optional[str] = Field(min_length=3, max_length=50)
    region_id: Optional[int] = Field(gt=0)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Update a department",
                    "description": "Update all the fields of a department with the following data",
                    "value": {
                        "name": "Chocó",
                        "region_id": 2
                    }
                },
                {
                    "summary": "Update the name of a department",
                    "description": "Update the name of a department",
                    "value": {
                        "name": "Chocó"
                    }
                },
                {
                    "summary": "Update the region of a department",
                    "description": "Update the region of a department",
                    "value": {
                        "region_id": 2
                    }
                }
            ]
        }
    }

