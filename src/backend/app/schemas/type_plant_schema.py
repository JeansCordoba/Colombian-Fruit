from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")

class TypePlantBase(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Nombre del tipo de planta")
    model_config = {
        "extra": "forbid",
    }

class TypePlantCreate(TypePlantBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Crear un tipo de planta",
                    "description": "Crear un tipo de planta con los siguientes datos",
                    "value": {
                        "name": "Árbol"
                    }
                }
            ]
        }
    }
    pass

class TypePlantResponse(TypePlantBase):
    type_plant_id: int = Field(gt=0)

class TypePlantUpdate(TypePlantBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Actualizar un tipo de planta",
                    "description": "Actualizar un tipo de planta con los siguientes datos",
                    "value": {
                        "name": "Árbol"
                    }
                }
            ]
        }
    }

class TypePlantSearch(OptionalField):
    type_plant_id: Optional[int] = Field(gt=0)
    name: Optional[str] = Field(min_length=3, max_length=50)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Buscar un tipo de planta",
                    "description": "Buscar un tipo de planta con los siguientes datos",
                    "value": {
                        "name": "Árbol"
                    }
                }
            ]
        }
    }