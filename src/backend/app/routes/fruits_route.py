from fastapi import APIRouter, Path, Body
from ..schemas import FruitCreate, FruitResponse, FruitSearch, FruitUpdate, FruitDetailResponse, FruitRegionResponse, FruitRegionDetailResponse, FruitRegionCreate
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

@router.get("/detail", response_model=list[FruitDetailResponse])
async def get_fruits_detail():
    fruits = FruitService.get_all_fruits()
    return fruits

@router.get("/{fruit_id}", response_model=FruitResponse)
async def get_fruit(fruit_id: int = Path(gt=0)):
    fruit = FruitService.get_fruit_by_id(fruit_id)
    return fruit

@router.get("/detail/{fruit_id}", response_model=FruitDetailResponse)
async def get_fruit_detail(fruit_id: int = Path(gt=0)):
    fruit = FruitService.get_fruit_by_id(fruit_id)
    return fruit

@router.get("/regions/{fruit_id}", response_model=list[FruitRegionResponse])
async def get_fruit_regions(fruit_id: int = Path(gt=0)):
    fruit_regions = FruitService.get_fruit_regions(fruit_id)
    return fruit_regions

@router.get("/regions/detail/{fruit_id}", response_model=list[FruitRegionDetailResponse])
async def get_fruit_regions_detail(fruit_id: int = Path(gt=0)):
    fruit_regions = FruitService.get_fruit_regions(fruit_id)
    return fruit_regions

@router.get("/search", response_model=list[FruitResponse])
async def search_fruits(search: FruitSearch = Body(...)):
    fruits = FruitService.search_fruits(search)
    return fruits

@router.get("/search/detail", response_model=list[FruitDetailResponse])
async def search_fruits_detail(search: FruitSearch = Body(...)):
    fruits = FruitService.search_fruits(search)
    return fruits

@router.patch("/{fruit_id}", response_model=FruitResponse)
async def update_fruit(fruit_id: int = Path(gt=0), update_data: FruitUpdate = Body(...)):
    fruit = FruitService.update_fruit(fruit_id, update_data)
    return fruit


@router.delete("/{fruit_id}", status_code=204)
async def delete_fruit(fruit_id: int = Path(gt=0)):
    FruitService.delete_fruit(fruit_id)
