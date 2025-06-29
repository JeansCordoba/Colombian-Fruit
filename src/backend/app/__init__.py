from fastapi import FastAPI
from .db import create_db_and_tables
from .routes import departments_route, fruits_route, regions_route, type_plant_route, family_route, fruit_region_route
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Build the FastAPI app
app = FastAPI(
    title="Colombian Fruits API",
    description="API to manage Colombian fruits",
    version="1.0.0",
    lifespan=lifespan
)

# Register the routes
app.include_router(fruits_route.router, prefix="/api/v1/fruits", tags=["fruits"])
app.include_router(departments_route.router, prefix="/api/v1/departments", tags=["departments"])
app.include_router(regions_route.router, prefix="/api/v1/regions", tags=["regions"])
app.include_router(type_plant_route.router, prefix="/api/v1/type-plants", tags=["type-plants"])
app.include_router(family_route.router, prefix="/api/v1/families", tags=["families"])
app.include_router(fruit_region_route.router, prefix="/api/v1/fruit-regions", tags=["fruit-regions"])