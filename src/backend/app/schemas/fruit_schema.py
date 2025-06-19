from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")

class FruitBase(BaseModel):
    common_name: str = Field(min_length=3, max_length=50, description="Nombre común de la fruta")
    scientific_name: str = Field(min_length=3, max_length=50, description="Nombre científico de la fruta")
    family_id: int = Field(gt=0, description="ID de la familia de la fruta")
    season: str = Field(min_length=3, max_length=50, description="Estación de la fruta")
    description: str = Field(min_length=3, max_length=1000, description="Descripción de la fruta")

class FruitCreate(FruitBase):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Crear una fruta",
                    "description": "Crear una fruta con los siguientes datos",
                    "value": {
                        "common_name": "Manzana",
                        "scientific_name": "Malus domestica",
                        "family_id": 1,
                        "season": "Invierno",
                        "description": "La manzana es una fruta de color rojo brillante y textura suave."
                    }
                }
            ]
        }
    }
    pass

class FruitResponse(FruitBase):
    fruit_id: int = Field(gt=0, description="ID de la fruta")

class FruitSearch(OptionalField):
    fruit_id: Optional[int] = Field(gt=0)
    common_name: Optional[str] = Field(min_length=3, max_length=50)
    scientific_name: Optional[str] = Field(min_length=3, max_length=50)
    family_id: Optional[int] = Field(gt=0)
    season: Optional[str] = Field(min_length=3, max_length=50)
 
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Buscar una fruta",
                    "description": "Buscar una fruta por su ID",
                    "value": {
                        "fruit_id": 1
                    }
                },
                {
                    "summary": "Buscar una fruta por su nombre común",
                    "description": "Buscar una fruta por su nombre común",
                    "value": {
                        "common_name": "Manzana"
                    }
                },
                {
                    "summary": "Buscar una fruta por su nombre científico",
                    "description": "Buscar una fruta por su nombre científico",
                    "value": {
                        "scientific_name": "Malus domestica"
                    }
                },
                {
                    "summary": "Buscar una fruta por su estación",
                    "description": "Buscar una fruta por su estación",
                    "value": {
                        "season": "Invierno"
                    }
                },
                {
                    "summary": "Buscar una fruta por su familia",
                    "description": "Buscar una fruta por su familia",
                    "value": {
                        "family_id": 1
                    }
                }
            ]
        }
    }

class FruitUpdate(OptionalField):
    common_name: Optional[str] = Field(min_length=3, max_length=50)
    scientific_name: Optional[str] = Field(min_length=3, max_length=50)
    family_id: Optional[int] = Field(gt=0)
    season: Optional[str] = Field(min_length=3, max_length=50)
    description: Optional[str] = Field(min_length=3, max_length=1000)
    
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Actualizar una fruta",
                    "description": "Actualizar una fruta con los siguientes datos",
                    "value": {
                        "common_name": "Manzana",
                        "scientific_name": "Malus domestica",
                        "family_id": 1,
                        "season": "Invierno",
                        "description": "La manzana es una fruta de color rojo brillante y textura suave."
                    }
                },
                {
                    "summary": "Actualizar el nombre común de una fruta",
                    "description": "Actualizar el nombre común de una fruta",
                    "value": {
                        "common_name": "Manzana"
                    }
                },
                {
                    "summary": "Actualizar el nombre científico de una fruta",
                    "description": "Actualizar el nombre científico de una fruta",
                    "value": {
                        "scientific_name": "Malus domestica"
                    }
                },
                {
                    "summary": "Actualizar la estación de una fruta",
                    "description": "Actualizar la estación de una fruta",
                    "value": {
                        "season": "Invierno"
                    }
                },
                {
                    "summary": "Actualizar la descripción de una fruta",
                    "description": "Actualizar la descripción de una fruta",
                    "value": {
                        "description": "La manzana es una fruta de color rojo brillante y textura suave."
                    }
                }
            ]
        }
    }