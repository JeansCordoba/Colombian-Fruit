from pydantic import BaseModel, Field

class FruitRegionBase(BaseModel):
    fruit_id: int = Field(gt=0, description="ID de la fruta")
    region_id: int = Field(gt=0, description="ID de la región")

    model_config = {
        "extra": "forbid",
    }
    
class FruitRegionResponse(FruitRegionBase):
    pass
    
class FruitRegionCreate(FruitRegionBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Crear una fruta en una región",
                    "description": "Crear una fruta en una región con los siguientes datos",
                    "value": {
                        "fruit_id": 1,
                        "region_id": 1,
                    }
                }
            ]
        }
    }

    
    
    