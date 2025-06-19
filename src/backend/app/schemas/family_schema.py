from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException


class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")

class FamilyBase(BaseModel):
    name: str = Field(index=True)
    type_plant_id: int = Field(gt=0, description="ID del tipo de planta de la familia")
    description: str = Field(min_length=3, max_length=1000, description="Descripción de la familia")

    model_config = {
        "extra": "forbid",
    }

class FamilyCreate(FamilyBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Crear una familia",
                    "description": "Crear una familia con los siguientes datos",
                    "value": {
                        "name": "Familia de las frutas",
                        "type_plant_id": 1,
                        "description": "Descripción de la familia"
                    }
                }
            ]
        }
    }
    
class FamilyResponse(FamilyBase):
    family_id: int = Field(gt=0)
  
class FamilySearch(OptionalField):
    family_id: Optional[int] = Field(gt=0)
    name: Optional[str] = Field(index=True)
    type_plant_id: Optional[int] = Field(gt=0)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Buscar una familia",
                    "description": "Buscar una familia por su nombre",
                    "value": {
                        "name": "Familia de las frutas"
                    }
                },
                {
                    "summary": "Buscar una familia por su ID",
                    "description": "Buscar una familia por su ID",
                    "value": {
                        "family_id": 1
                    }
                },
                {
                    "summary": "Buscar una familia por su tipo de planta",
                    "description": "Buscar una familia por su tipo de planta",
                    "value": {
                        "type_plant_id": 1
                    }
                }
            ]
        }
    }

class FamilyUpdate(OptionalField):
    name: Optional[str] = Field(index=True)
    type_plant_id: Optional[int] = Field(gt=0)
    description: Optional[str] = Field(min_length=3, max_length=1000)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Actualizar una familia",
                    "description": "Actualizar una familia con los siguientes datos",
                    "value": {
                        "name": "Familia de las frutas",
                        "type_plant_id": 1,
                        "description": "Descripción de la familia"
                    }
                },
                {
                    "summary": "Actualizar el nombre de una familia",
                    "description": "Actualizar el nombre de una familia",
                    "value": {
                        "name": "Familia de las frutas"
                    }
                },
                {
                    "summary": "Actualizar el tipo de planta de una familia",
                    "description": "Actualizar el tipo de planta de una familia",
                    "value": {
                        "type_plant_id": 1
                    }
                },
                {
                    "summary": "Actualizar la descripción de una familia",
                    "description": "Actualizar la descripción de una familia",
                    "value": {
                        "description": "Descripción de la familia"
                    }
                }
            ]
        }
    }
    
