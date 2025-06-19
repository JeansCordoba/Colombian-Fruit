from sqlmodel import Field, SQLModel

class TypePlant(SQLModel, table=True):
    type_plant_id: int = Field(primary_key=True, nullable=False)
    name: str = Field(index=True)
    
    def __repr__(self):
        return f"<TypePlant {self.name}>"
    