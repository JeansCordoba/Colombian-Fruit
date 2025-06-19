from sqlmodel import Field, SQLModel

class FruitRegion(SQLModel, table=True):
    fruit_id: int = Field(primary_key=True, foreign_key="fruit.fruit_id", description="ID de la fruta")
    region_id: int = Field(primary_key=True, foreign_key="region.region_id", description="ID de la región")
    
    def __repr__(self):
        return f"<FruitRegion {self.fruit_id} - {self.region_id}>"
    