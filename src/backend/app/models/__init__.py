# Modelos base (sin dependencias)
from .type_plant_model import TypePlant
from .region_model import Region

# Modelos que dependen de los base
from .family_model import Family  # Depende de TypePlant
from .department_model import Department  # Depende de Region

# Modelos con relaciones many-to-many
from .fruit_model import Fruit  # Depende de Family
from .fruit_region_model import FruitRegion  # Depende de Fruit y Region

__all__ = ["Department", "Family", "FruitRegion", "Fruit", "Region", "TypePlant"]