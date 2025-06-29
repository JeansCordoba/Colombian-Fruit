from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

class OptionalField(BaseModel):
    def __init__(self, **data):
        super().__init__(**data)
        if all(value is None for value in data.values()):
            raise HTTPException(status_code=400, detail="At least one field must be provided")

class RegionBase(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the region")
    weather: str = Field(min_length=3, max_length=50, description="Weather of the region")
    altitude: int = Field(gt=0, le=5000, description="Altitude of the region in meters")


class RegionCreate(RegionBase):
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                "summary": "Create a region",
                "description": "Create a region with the following data",
                "value": {
                    "name": "Andes",
                    "weather": "Temperate",
                    "altitude": 1000
                }
            }
            ]
        }
    }

class RegionResponse(RegionBase):
    region_id: int = Field(gt=0)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Region data",
                    "description": "Returns the data of a region",
                    "value": {
                        "region_id": 1,
                        "name": "Andes",
                        "weather": "Temperate",
                        "altitude": 1000
                    }
                }
            ]
        }
    }

class RegionUpdate(OptionalField):
    name: Optional[str] = Field(min_length=3, max_length=50)
    weather: Optional[str] = Field(min_length=3, max_length=50)
    altitude: Optional[int] = Field(gt=0, le=5000)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Update a region",
                    "description": "Update all the fields of a region with the following data",
                    "value": {
                        "name": "Andes",
                        "weather": "Temperate",
                        "altitude": 1000
                    }
                },
                {
                    "summary": "Update the name of a region",
                    "description": "Update the name of a region",
                    "value": {
                        "name": "Andes"
                    }
                },
                {
                    "summary": "Update the weather of a region",
                    "description": "Update the weather of a region",
                    "value": {
                        "weather": "Temperate"
                    }
                },
                {
                    "summary": "Update the altitude of a region",
                    "description": "Update the altitude of a region",
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
                    "summary": "Search by region_id",
                    "description": "Search a region by its ID",
                    "value": {
                        "region_id": 1
                    }
                },
                {
                    "summary": "Search by name",
                    "description": "Search a region by its name",
                    "value": {
                        "name": "Andes"
                    }
                },
                {
                    "summary": "Search by weather",
                    "description": "Search a region by its weather",
                    "value": {
                        "weather": "Temperate"
                    }
                },
                {
                    "summary": "Search by altitude",
                    "description": "Search a region by its altitude",
                    "value": {
                        "altitude": 1000
                    }
                }
            ]
        }
    }
