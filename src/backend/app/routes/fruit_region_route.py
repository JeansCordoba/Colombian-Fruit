from fastapi import APIRouter, Path, Body
from ..schemas import FruitRegionCreate, FruitRegionResponse
from ..services import FruitRegionService

router = APIRouter()

@router.post("/", response_model=FruitRegionResponse)
async def add_region_to_fruit(fruit_region: FruitRegionCreate = Body(...)):
    return FruitRegionService.create_fruit_region(fruit_region)

@router.get("/", response_model=list[FruitRegionResponse])
async def get_all_fruit_regions():
    return FruitRegionService.get_all_fruit_regions()

@router.delete("/", status_code=204)
async def delete_fruit_region(fruit_id: int = Path(gt=0), region_id: int = Path(gt=0)):
    FruitRegionService.delete_fruit_region(fruit_id, region_id) 