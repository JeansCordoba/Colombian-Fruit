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

class TypePlantResponse(TypePlantBase):
    type_plant_id: int = Field(gt=0)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Datos de tipo de planta (vista de BD)",
                    "description": "Muestra los datos de un tipo de planta como vista de la base de datos",
                    "value": {
                        "type_plant_id": 1,
                        "name": "Árbol"
                    }
                }
            ]
        }
    }

class TypePlantDetailResponse(BaseModel):
    name: str = Field(description="Nombre del tipo de planta")
    model_config = {
        "extra": "ignore",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Datos de tipo de planta (vista de usuario)",
                    "description": "Muestra los datos de el nombre del tipo de planta",
                    "value": {
                        "name": "Árbol"
                    }
                }
            ]
        }
    }

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
                    "description": "Buscar un tipo de planta por nombre con los siguientes datos",
                    "value": {
                        "type_plant_id": 1,
                        "name": "Árbol"
                    }
                },
                {
                    "summary": "Buscar un tipo de planta por ID",
                    "description": "Buscar un tipo de planta por ID",
                    "value": {
                        "type_plant_id": 1
                    }
                },
                {
                    "summary": "Buscar un tipo de planta por nombre",
                    "description": "Buscar un tipo de planta por nombre",
                    "value": {
                        "name": "Árbol"
                    }
                }
            ]
        }
    }