from sqlmodel import Field, SQLModel, Relationship
from .fruit_region_model import FruitRegion

class Fruit(SQLModel, table=True):
    fruit_id: int = Field(primary_key=True, nullable=False)
    common_name: str = Field(
        min_length=3,
        max_length=50,
        description="Nombre común de la fruta",
        index=True
    )
    scientific_name: str = Field(
        min_length=3,
        max_length=50,
        description="Nombre científico de la fruta"
    )
    family_id: int = Field(
        gt=0,
        description="ID de la familia de la fruta",
        foreign_key="family.family_id"
    )
    season: str = Field(
        min_length=3,
        max_length=50,
        description="Estación de la fruta"
    )
    description: str = Field(
        min_length=3,
        max_length=1000,
        description="Descripción de la fruta"
    )
    
    # Relaciones
    family: "Family" = Relationship(back_populates="fruits")
    regions: list["Region"] = Relationship(
        back_populates="fruits",
        link_model=FruitRegion,
        sa_relationship_kwargs={
            "primaryjoin": "Fruit.fruit_id == FruitRegion.fruit_id",
            "secondaryjoin": "Region.region_id == FruitRegion.region_id"
        }
    )
    
    def __repr__(self):
        return f"<Fruit {self.common_name}>"
    