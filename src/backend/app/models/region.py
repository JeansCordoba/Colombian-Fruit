from sqlmodel import Field, SQLModel, Relationship
from .fruit_region import FruitRegion
class Region(SQLModel, table=True):
    region_id: int = Field(primary_key=True, nullable=False)
    name: str = Field(
        min_length=3,
        max_length=50,
        description="Nombre de la región",
        index=True
    )
    weather: str = Field(
        min_length=3,
        max_length=50,
        description="Clima de la región"
    )
    altitude: int = Field(
        gt=0,
        le=5000,
        description="Altura de la región en metros"
    )
    
    # Relaciones
    fruits: list["Fruit"] = Relationship(back_populates="regions", link_model=FruitRegion)
    departments: list["Department"] = Relationship(back_populates="region")
    
    def __repr__(self):
        return f"<Region {self.name}>"