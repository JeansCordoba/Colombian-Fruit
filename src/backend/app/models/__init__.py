# Base models (without dependencies)
from .type_plant_model import TypePlant
from .region_model import Region

# Models that depend on the base models
from .family_model import Family  # TypePlant depends of Family
from .department_model import Department  # Region depends of Department

# Models with many-to-many relationships
from .fruit_model import Fruit  # Family depends of Fruit
from .fruit_region_model import FruitRegion  # Fruit and Region depends of FruitRegion

__all__ = ["Department", "Family", "FruitRegion", "Fruit", "Region", "TypePlant"]