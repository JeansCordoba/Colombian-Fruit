from fastapi import APIRouter, Path, Body
from ..schemas import FamilyCreate, FamilyUpdate, FamilySearch, FamilyResponse
from ..services import FamilyService

router = APIRouter()

@router.post("/", response_model=FamilyResponse)
async def create_family(family: FamilyCreate = Body(...)):
    family = FamilyService.create_family(family)
    return family

@router.get("/", response_model=list[FamilyResponse])
async def get_families():
    families = FamilyService.get_all_families()
    return families

@router.get("/{family_id}", response_model=FamilyResponse)
async def get_family(family_id: int = Path(gt=0)):
    family = FamilyService.get_family_by_id(family_id)
    return family

@router.get("/search", response_model=list[FamilyResponse])
async def search_families(search: FamilySearch = Body(...)):
    families = FamilyService.search_families(search)
    return families

@router.patch("/{family_id}", response_model=FamilyResponse)
async def update_family(family_id: int = Path(gt=0), update_data: FamilyUpdate = Body(...)):
    family = FamilyService.update_family(family_id, update_data)
    return family

@router.delete("/{family_id}", status_code=204)
async def delete_family(family_id: int = Path(gt=0)):
    FamilyService.delete_family(family_id)
