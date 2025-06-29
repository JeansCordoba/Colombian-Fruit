from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")

class TypePlantBase(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the type of plant")
    model_config = {
        "extra": "forbid",
    }

class TypePlantCreate(TypePlantBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Create a type of plant",
                    "description": "Create a type of plant with the following data",
                    "value": {
                        "name": "Tree"
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
                    "summary": "Type plant data",
                    "description": "Returns the data of a type of plant",
                    "value": {
                        "type_plant_id": 1,
                        "name": "Tree"
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
                    "summary": "Update a type of plant",
                    "description": "Update a type of plant with the following data",
                    "value": {
                        "name": "Tree"
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
                    "summary": "Search by type_plant_id",
                    "description": "Search a type of plant by its ID",
                    "value": {
                        "type_plant_id": 1,
                        "name": "Tree"
                    }
                },
                {
                    "summary": "Search by type_plant_id",
                    "description": "Search a type of plant by its ID",
                    "value": {
                        "type_plant_id": 1
                    }
                },
                {
                    "summary": "Search by name",
                    "description": "Search a type of plant by its name",
                    "value": {
                        "name": "Tree"
                    }
                }
            ]
        }
    }