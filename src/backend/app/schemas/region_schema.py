from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")

class RegionBase(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Nombre de la región")
    weather: str = Field(min_length=3, max_length=50, description="Clima de la región")
    altitude: int = Field(gt=0, le=5000, description="Altura de la región en metros")


class RegionCreate(RegionBase):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                "summary": "Crear una región",
                "description": "Crear una región con los siguientes datos",
                "value": {
                    "name": "Andes",
                    "weather": "Templado",
                    "altitude": 1000
                }
            }
            ]
        }
    }
    pass

class RegionResponse(RegionBase):
    region_id: int = Field(gt=0)
    
class RegionUpdate(OptionalField):
    name: Optional[str] = Field(min_length=3, max_length=50)
    weather: Optional[str] = Field(min_length=3, max_length=50)
    altitude: Optional[int] = Field(gt=0, le=5000)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Actualizar una región",
                    "description": "Actualizar todos los campos de una región con los siguientes datos",
                    "value": {
                        "name": "Andes",
                        "weather": "Templado",
                        "altitude": 1000
                    }
                },
                {
                    "summary": "Actualizar el nombre de una región",
                    "description": "Actualizar el nombre de una región",
                    "value": {
                        "name": "Andes"
                    }
                },
                {
                    "summary": "Actualizar el clima de una región",
                    "description": "Actualizar el clima de una región",
                    "value": {
                        "weather": "Templado"
                    }
                },
                {
                    "summary": "Actualizar la altitud de una región",
                    "description": "Actualizar la altitud de una región",
                    "value": {
                        "altitude": 1000
                    }
                }
            ]
        }
    }
    
class RegionSearch(OptionalField):
    region_id: Optional[int] = Field(gt=0)
    name: Optional[str] = Field(min_length=3, max_length=50)
    weather: Optional[str] = Field(min_length=3, max_length=50)
    altitude: Optional[int] = Field(gt=0, le=5000)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Buscar por region_id",
                    "description": "Buscar una región por su ID",
                    "value": {
                        "region_id": 1
                    }
                },
                {
                    "summary": "Buscar por nombre",
                    "description": "Buscar una región por su nombre",
                    "value": {
                        "name": "Andes"
                    }
                },
                {
                    "summary": "Buscar por clima",
                    "description": "Buscar una región por su clima",
                    "value": {
                        "weather": "Templado"
                    }
                },
                {
                    "summary": "Buscar por altitud",
                    "description": "Buscar una región por su altitud",
                    "value": {
                        "altitude": 1000
                    }
                }
            ]
        }
    }
