from pydantic import BaseModel, Field

class FruitRegionBase(BaseModel):
    fruit_id: int = Field(gt=0, description="ID de la fruta")
    region_id: int = Field(gt=0, description="ID de la región")

    model_config = {
        "extra": "forbid",
    }
    
class FruitRegionResponse(FruitRegionBase):
    model_config = {
        "extra": "ignore",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Datos de fruta en una región (vista de BD)",
                    "description": "Muestra los datos de una fruta en una región como vista de la base de datos",
                    "value": {
                        "fruit_id": 1,
                        "region_id": 1,
                    }
                }
            ]
        }
    }

class FruitRegionDetailResponse(BaseModel):
    fruit_name: str = Field(description="Nombre de la fruta")
    region_name: str = Field(description="Nombre de la región")
    
    model_config = {
        "extra": "ignore",
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Datos de fruta en una región (vista de usuario)",
                    "description": "Muestra los datos de el nombre de la fruta y el nombre de la región a la que pertenece",
                    "value": {
                        "fruit_name": "Manzana",
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
