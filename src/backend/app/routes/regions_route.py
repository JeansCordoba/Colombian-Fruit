from fastapi import APIRouter, Path, Body
from ..schemas import RegionCreate, RegionUpdate, RegionSearch, RegionResponse, RegionDetailResponse, FruitRegionResponse, FruitRegionDetailResponse
from ..services import RegionService

router = APIRouter()

@router.post("/", response_model=RegionResponse)
async def create_region(region: RegionCreate = Body(...)):
    region = RegionService.create_region(region)
    return region

@router.get("/", response_model=list[RegionResponse])
async def get_regions():
    regions = RegionService.get_all_regions()
    return regions

@router.get("/detail", response_model=list[RegionDetailResponse])
async def get_regions_detail():
    regions = RegionService.get_all_regions()
    return regions

@router.get("/{region_id}", response_model=RegionResponse)
async def get_region(region_id: int = Path(gt=0)):
    region = RegionService.get_region_by_id(region_id)
    return region

@router.get("/detail/{region_id}", response_model=RegionDetailResponse)
async def get_region_detail(region_id: int = Path(gt=0)):
    region = RegionService.get_region_by_id(region_id)
    return region

@router.get("/fruits/{region_id}", response_model=list[FruitRegionResponse])
async def get_region_fruits(region_id: int = Path(gt=0)):
    region_fruits = RegionService.get_region_fruits(region_id)
    return region_fruits

@router.get("/fruits/detail/{region_id}", response_model=list[FruitRegionDetailResponse])
async def get_region_fruits_detail(region_id: int = Path(gt=0)):
    region_fruits = RegionService.get_region_fruits(region_id)
    return region_fruits

@router.get("/search", response_model=list[RegionResponse])
async def search_regions(search: RegionSearch = Body(...)):
    regions = RegionService.search_regions(search)
    return regions

@router.get("/search/detail", response_model=list[RegionDetailResponse])
async def search_regions_detail(search: RegionSearch = Body(...)):
    regions = RegionService.search_regions(search)
    return regions

@router.patch("/{region_id}", response_model=RegionResponse)
async def update_region(region_id: int = Path(gt=0), update_data: RegionUpdate = Body(...)):
    region = RegionService.update_region(region_id, update_data)
    return region

@router.delete("/{region_id}", status_code=204)
async def delete_region(region_id: int = Path(gt=0)):
    RegionService.delete_region(region_id)