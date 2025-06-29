from fastapi import APIRouter, Path, Body
from ..schemas import TypePlantResponse, TypePlantCreate, TypePlantUpdate, TypePlantSearch
from ..services import TypePlantService

router = APIRouter()

@router.post("/", response_model=TypePlantResponse)
async def create_type_plant(type_plant: TypePlantCreate):
    type_plant = TypePlantService.create_type_plant(type_plant)
    return type_plant

@router.get("/", response_model=list[TypePlantResponse])
async def get_types_plants():
    type_plants = TypePlantService.get_all_type_plants()
    return type_plants

@router.get("/{type_plant_id}", response_model=TypePlantResponse)
async def get_type_plant(type_plant_id: int = Path(gt=0)):
    type_plant = TypePlantService.get_type_plant_by_id(type_plant_id)
    return type_plant

@router.get("/search", response_model=list[TypePlantResponse])
async def search_type_plants(search: TypePlantSearch = Body(...)):
    type_plants = TypePlantService.search_type_plants(search)
    return type_plants

@router.patch("/{type_plant_id}", response_model=TypePlantResponse)
async def update_type_plant(type_plant_id: int = Path(gt=0), update_data: TypePlantUpdate = Body(...)):
    type_plant = TypePlantService.update_type_plant(type_plant_id, update_data)
    return type_plant

@router.delete("/{type_plant_id}", status_code=204)
async def delete_type_plant(type_plant_id: int = Path(gt=0)):
    TypePlantService.delete_type_plant(type_plant_id)