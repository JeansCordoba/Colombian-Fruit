from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class DepartmentBase(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Nombre del departamento")
    region_id: int = Field(gt=0, description="ID de la región del departamento")
    

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")
    
class DepartmentCreate(DepartmentBase):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                "summary": "Crear un departamento",
                "description": "Crear un departamento con los siguientes datos",
                    "value": {
                        "name": "Chocó",
                        "region_id": 2
                    }
                }
            ]
        }
    }
    pass

class DepartmentResponse(DepartmentBase):
    department_id: int = Field(gt=0)
    

class DepartmentSearch(OptionalField):
    department_id: Optional[int] = Field(gt=0)
    name: Optional[str] = Field(min_length=3, max_length=50)
    region_id: Optional[int] = Field(gt=0)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Buscar por department_id",
                    "description": "Buscar un departamento por su ID",
                    "value": {
                        "department_id": 1
                    }
                },
                {
                    "summary": "Buscar por nombre",
                    "description": "Buscar un departamento por su nombre",
                    "value": {
                        "name": "Chocó"
                    }
                },
                {
                    "summary": "Buscar por region_id",
                    "description": "Buscar un departamento por su ID de región",
                    "value": {
                        "region_id": 2
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
                    "summary": "Actualizar un departamento",
                    "description": "Actualizar todos los campos de un departamento con los siguientes datos",
                    "value": {
                        "name": "Chocó",
                        "region_id": 2
                    }
                },
                {
                    "summary": "Actualizar el nombre de un departamento",
                    "description": "Actualizar el nombre de un departamento",
                    "value": {
                        "name": "Chocó"
                    }
                },
                {
                    "summary": "Actualizar la región de un departamento",
                    "description": "Actualizar la región de un departamento",
                    "value": {
                        "region_id": 2
                    }
                }
            ]
        }
    }

