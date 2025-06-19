from fastapi import APIRouter, Path, Body
from ..schemas import FruitRegionCreate, FruitRegionResponse
from ..services import FruitRegionService

router = APIRouter()

@router.post("/", response_model=FruitRegionResponse)
async def create_fruit_region(fruit_region: FruitRegionCreate = Body(...)):
    """
    Crear una relación entre una fruta y una región
    """
    return FruitRegionService.create_fruit_region(fruit_region)

@router.delete("/", status_code=204)
async def delete_fruit_region(fruit_id: int = Path(gt=0), region_id: int = Path(gt=0)):
    """
    Eliminar la relación entre una fruta y una región
    """
    FruitRegionService.delete_fruit_region(fruit_id, region_id) 