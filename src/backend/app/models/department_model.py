from sqlmodel import Field, SQLModel, Relationship

class Department(SQLModel, table=True):
    department_id: int = Field(primary_key=True, nullable=False)
    name: str 
    region_id: int = Field(foreign_key="region.region_id")
    
    # Relationships
    region: "Region" = Relationship(back_populates="departments")
    
    def __repr__(self):
        return f"<Department {self.name}>"
