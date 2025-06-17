from fastapi import FastAPI

# Crear la aplicación FastAPI
app = FastAPI(
    title="Colombian Fruits API",
    description="API para gestionar frutas colombianas",
    version="1.0.0"
)


# Luego importar las rutas
from app.routes import fruits, departments

# Registrar las rutas
app.include_router(fruits.router, prefix="/api/v1", tags=["fruits"])
app.include_router(departments.router, prefix="/api/v1", tags=["departments"])
