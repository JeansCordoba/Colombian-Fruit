from fastapi import APIRouter, Path, Body
from ..schemas import FruitCreate, FruitResponse, FruitSearch, FruitUpdate
from ..services import FruitService

router = APIRouter()

@router.post("/", response_model=FruitResponse)
async def create_fruit(fruit: FruitCreate = Body(...)):
    fruit = FruitService.create_fruit(fruit)
    return fruit

@router.get("/", response_model=list[FruitResponse])
async def get_fruits():
    fruits = FruitService.get_all_fruits()
    return fruits

@router.get("/{fruit_id}", response_model=FruitResponse)
async def get_fruit(fruit_id: int = Path(gt=0)):
    fruit = FruitService.get_fruit_by_id(fruit_id)
    return fruit

@router.get("/search", response_model=list[FruitResponse])
async def search_fruits(search: FruitSearch = Body(...)):
    fruits = FruitService.search_fruits(search)
    return fruits

@router.patch("/{fruit_id}", response_model=FruitResponse)
async def update_fruit(fruit_id: int = Path(gt=0), update_data: FruitUpdate = Body(...)):
    fruit = FruitService.update_fruit(fruit_id, update_data)
    return fruit

@router.delete("/{fruit_id}", status_code=204)
async def delete_fruit(fruit_id: int = Path(gt=0)):
    FruitService.delete_fruit(fruit_id)
