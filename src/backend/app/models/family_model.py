from sqlmodel import Field, SQLModel, Relationship

class Family(SQLModel, table=True):
    family_id: int = Field(primary_key=True, nullable=False)
    name: str = Field(index=True)
    type_plant_id: int
    description: str 
    # Relaciones
    fruits: list["Fruit"] = Relationship(back_populates="family")
    
    def __repr__(self):
        return f"<Family {self.name}>"
    