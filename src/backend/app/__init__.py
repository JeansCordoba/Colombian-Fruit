from fastapi import FastAPI
from app.db.database import create_db_and_tables
from app.routes import departments_route, fruits_route, regions_route

# Crear la aplicación FastAPI
app = FastAPI(
    title="Colombian Fruits API",
    description="API para gestionar frutas colombianas",
    version="1.0.0"
)

# Crear las tablas al iniciar la aplicación
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Registrar las rutas
app.include_router(fruits_route.router, prefix="/api/v1", tags=["fruits"])
app.include_router(departments_route.router, prefix="/api/v1", tags=["departments"])
app.include_router(regions_route.router, prefix="/api/v1", tags=["regions"])
