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

class FamilyBase(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the family")
    type_plant_id: int = Field(gt=0, description="ID of the type of plant of the family")
    description: str = Field(min_length=3, max_length=1000, description="Description of the family")

    model_config = {
        "extra": "forbid",
    }

class FamilyCreate(FamilyBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Create a family",
                    "description": "Create a family with the following data",
                    "value": {
                        "name": "Fruit family",
                        "type_plant_id": 1,
                        "description": "Description of the family"
                    }
                }
            ]
        }
    }
    
class FamilyResponse(FamilyBase):
    family_id: int = Field(gt=0)
    type_plant_name: str = Field(min_length=3, max_length=50, description="Name of the type of plant")
    model_config = {
        "extra": "ignore",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Family data",
                    "description": "Returns the data of a family",
                    "value": {
                        "family_id": 1,
                        "name": "Fruit family",
                        "type_plant_id": 1,
                        "type_plant_name": "Tree",
                        "description": "Description of the family"
                    }
                }
            ]
        }
    }
     
  
class FamilySearch(OptionalField):
    family_id: Optional[int] = Field(gt=0)
    name: Optional[str] = Field(min_length=3, max_length=50)
    type_plant_id: Optional[int] = Field(gt=0)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Search by name",
                    "description": "Search a family by its name",
                    "value": {
                        "name": "Fruit family"
                    }
                },
                {
                    "summary": "Search by family_id",
                    "description": "Search a family by its ID",
                    "value": {
                        "family_id": 1
                    }
                },
                {
                    "summary": "Search by type_plant_id",
                    "description": "Search a family by its type of plant ID",
                    "value": {
                        "type_plant_id": 1
                    }
                }
            ]
        }
    }

class FamilyUpdate(OptionalField):
    name: Optional[str] = Field(min_length=3, max_length=50)
    type_plant_id: Optional[int] = Field(gt=0)
    description: Optional[str] = Field(min_length=3, max_length=1000)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Update a family",
                    "description": "Update a family with the following data",
                    "value": {
                        "name": "Fruit family",
                        "type_plant_id": 1,
                        "description": "Description of the family"
                    }
                },
                {
                    "summary": "Update the name of a family",
                    "description": "Update the name of a family",
                    "value": {
                        "name": "Fruit family"
                    }
                },
                {
                    "summary": "Update the type of plant of a family",
                    "description": "Update the type of plant of a family",
                    "value": {
                        "type_plant_id": 1
                    }
                },
                {
                    "summary": "Update the description of a family",
                    "description": "Update the description of a family",
                    "value": {
                        "description": "Description of the family"
                    }
                }
            ]
        }
    }
    
