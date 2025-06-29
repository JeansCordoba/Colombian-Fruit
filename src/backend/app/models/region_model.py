from sqlmodel import Field, SQLModel, Relationship
from .fruit_region_model import FruitRegion

class Region(SQLModel, table=True):
    region_id: int = Field(primary_key=True, nullable=False)
    name: str = Field(index=True)
    weather: str
    altitude: int
    
    # Relationships
    fruits: list["Fruit"] = Relationship(
        back_populates="regions",
        link_model=FruitRegion,
        sa_relationship_kwargs={
            "primaryjoin": "Region.region_id == FruitRegion.region_id",
            "secondaryjoin": "Fruit.fruit_id == FruitRegion.fruit_id"
        }
    )
    departments: list["Department"] = Relationship(
        back_populates="region",
        sa_relationship_kwargs={
            "primaryjoin": "Region.region_id == Department.region_id"
        }
    )
    
    def __repr__(self):
        return f"<Region {self.name}>"