from fastapi import APIRouter, Path, Body
from ..schemas import RegionCreate, RegionUpdate, RegionSearch, RegionResponse
from ..services import RegionService

router = APIRouter()

@router.get("/", response_model=list[RegionResponse])
async def get_regions():
    regions = RegionService.get_all_regions()
    return regions

@router.get("/{region_id}", response_model=RegionResponse)
async def get_region(region_id: int = Path(gt=0)):
    region = RegionService.get_region_by_id(region_id)
    return region

@router.get("/search", response_model=list[RegionResponse])
async def search_regions(search: RegionSearch = Body(...)):
    regions = RegionService.search_regions(search)
    return regions

@router.post("/", response_model=RegionResponse)
async def create_region(region: RegionCreate = Body(...)):
    region = RegionService.create_region(region)
    return region

@router.patch("/{region_id}", response_model=RegionResponse)
async def update_region(region_id: int = Path(gt=0), update_data: RegionUpdate = Body(...)):
    region = RegionService.update_region(region_id, update_data)
    return region

@router.delete("/{region_id}", status_code=204)
async def delete_region(region_id: int = Path(gt=0)):
    RegionService.delete_region(region_id)