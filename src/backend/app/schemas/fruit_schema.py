from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")

class FruitBase(BaseModel):
    common_name: str = Field(min_length=3, max_length=50, description="Common name of the fruit")
    scientific_name: str = Field(min_length=3, max_length=50, description="Scientific name of the fruit")
    family_id: int = Field(gt=0, description="ID of the family of the fruit")
    season: str = Field(min_length=3, max_length=50, description="Season of the fruit")
    description: str = Field(min_length=3, max_length=1000, description="Description of the fruit")

class FruitCreate(FruitBase):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Create a fruit",
                    "description": "Create a fruit with the following data",
                    "value": {
                        "common_name": "Apple",
                        "scientific_name": "Malus domestica",
                        "family_id": 1,
                        "season": "Winter",
                        "description": "The apple is a red and soft fruit."
                    }
                }
            ]
        }
    }
    pass

class FruitResponse(FruitBase):
    fruit_id: int = Field(gt=0, description="ID of the fruit")
    family_name: str = Field(min_length=3, max_length=50, description="Name of the family of the fruit")
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Fruit data",
                    "description": "Returns the data of a fruit",
                    "value": {
                        "fruit_id": 1,
                        "common_name": "Apple",
                        "scientific_name": "Malus domestica",
                        "family_id": 1,
                        "family_name": "Malus",
                        "season": "Winter",
                        "description": "The apple is a red and soft fruit."
                    }
                }
            ]
        }
    }


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
                    "summary": "Search by fruit_id",
                    "description": "Search a fruit by its ID",
                    "value": {
                        "fruit_id": 1
                    }
                },
                {
                    "summary": "Search by common_name",
                    "description": "Search a fruit by its common name",
                    "value": {
                        "common_name": "Apple"
                    }
                },
                {
                    "summary": "Search by scientific_name",
                    "description": "Search a fruit by its scientific name",
                    "value": {
                        "scientific_name": "Malus domestica"
                    }
                },
                {
                    "summary": "Search by season",
                    "description": "Search a fruit by its season",
                    "value": {
                        "season": "Winter"
                    }
                },
                {
                    "summary": "Search by family_id",
                    "description": "Search a fruit by its family ID",
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
                    "summary": "Update a fruit",
                    "description": "Update a fruit with the following data",
                    "value": {
                        "common_name": "Apple",
                        "scientific_name": "Malus domestica",
                        "family_id": 1,
                        "season": "Winter",
                        "description": "The apple is a red and soft fruit."
                    }
                },
                {
                    "summary": "Update the common name of a fruit",
                    "description": "Update the common name of a fruit",
                    "value": {
                        "common_name": "Apple"
                    }
                },
                {
                    "summary": "Update the scientific name of a fruit",
                    "description": "Update the scientific name of a fruit",
                    "value": {
                        "scientific_name": "Malus domestica"
                    }
                },
                {
                    "summary": "Update the season of a fruit",
                    "description": "Update the season of a fruit",
                    "value": {
                        "season": "Winter"
                    }
                },
                {
                    "summary": "Update the description of a fruit",
                    "description": "Update the description of a fruit",
                    "value": {
                        "description": "The apple is a red and soft fruit."
                    }
                }
            ]
        }
    }