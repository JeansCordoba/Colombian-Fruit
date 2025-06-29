from sqlmodel import Field, SQLModel, Relationship
from .fruit_region_model import FruitRegion

class Fruit(SQLModel, table=True):
    fruit_id: int = Field(primary_key=True, nullable=False)
    common_name: str = Field(index=True)
    scientific_name: str = Field(index=True)
    family_id: int = Field(foreign_key="family.family_id")
    season: str = Field(index=True)
    description: str = Field(index=True)
    
    # Relationships
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
    