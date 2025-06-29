from pydantic import BaseModel, Field

class FruitRegionBase(BaseModel):
    fruit_id: int = Field(gt=0, description="ID de la fruta")
    region_id: int = Field(gt=0, description="ID de la región")

    model_config = {
        "extra": "forbid",
    }
    
class FruitRegionResponse(FruitRegionBase):
    fruit_name: str = Field(min_length=3, max_length=50, description="Name of the fruit")
    region_name: str = Field(min_length=3, max_length=50, description="Name of the region")
    model_config = {
        "extra": "ignore",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Fruit region data",
                    "description": "Returns the data of a fruit in a region",
                    "value": {
                        "fruit_id": 1,
                        "region_id": 1,
                        "fruit_name": "Apple",
                        "region_name": "Chocó",
                    }
                }
            ]
        }
    }

class FruitRegionCreate(FruitRegionBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Create a fruit in a region",
                    "description": "Create a fruit in a region with the following data",
                    "value": {
                        "fruit_id": 1,
                        "region_id": 1,
                    }
                }
            ]
        }
    }
