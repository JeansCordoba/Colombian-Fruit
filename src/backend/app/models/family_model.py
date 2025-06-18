from sqlmodel import Field, SQLModel, Relationship

class Family(SQLModel, table=True):
    family_id: int = Field(primary_key=True, nullable=False)
    name: str = Field(
        min_length=3,
        max_length=50,
        description="Nombre de la familia",
        index=True
    )
    type_plant_id: int = Field(
        gt=0,
        description="ID del tipo de planta de la familia",
        foreign_key="typeplant.type_plant_id"
    )
    description: str = Field(
        min_length=3,
        max_length=1000,
        description="Descripción de la familia"
    )
    
    # Relaciones
    fruits: list["Fruit"] = Relationship(back_populates="family")
    
    def __repr__(self):
        return f"<Family {self.name}>"
    