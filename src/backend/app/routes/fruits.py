from fastapi import APIRouter
from app.db.database import get_session
from app.models import Fruit


router = APIRouter()

@router.get("/fruits")
async def get_fruits():
    return {"message": "Lista de frutas colombianas"}

