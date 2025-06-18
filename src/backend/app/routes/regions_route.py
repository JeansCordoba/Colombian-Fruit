from fastapi import APIRouter, Path, Body
from app.schemas import RegionCreate, RegionUpdate, RegionSearch, RegionResponse
from app.services import RegionService

router = APIRouter()

@router.get("/regions", response_model=list[RegionResponse])
def get_regions():
    regions = RegionService.get_all_regions()
    return regions

@router.get("/regions/{region_id}", response_model=RegionResponse)
def get_region(region_id: int = Path(gt=0)):
    region = RegionService.get_region_by_id(region_id)
    return region

@router.get("/regions/search", response_model=list[RegionResponse])
def search_regions(search: RegionSearch = Body(...)):
    regions = RegionService.get_regions(search)
    return regions

@router.post("/regions", response_model=RegionResponse)
def create_region(region: RegionCreate = Body(...)):
    region = RegionService.create_region(region)
    return region

@router.patch("/regions/{region_id}", response_model=RegionResponse)
def update_region(region_id: int = Path(gt=0), update_data: RegionUpdate = Body(...)):
    region = RegionService.update_region(region_id, update_data)
    return region

@router.delete("/regions/{region_id}", status_code=204)
def delete_region(region_id: int = Path(gt=0)):
    RegionService.delete_region(region_id)
    return