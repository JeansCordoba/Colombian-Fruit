# Modelos base (sin dependencias)
from .type_plant import TypePlant
from .region import Region

# Modelos que dependen de los base
from .family import Family  # Depende de TypePlant
from .department import Department  # Depende de Region

# Modelos con relaciones many-to-many
from .fruit import Fruit  # Depende de Family
from .fruit_region import FruitRegion  # Depende de Fruit y Region

__all__ = ["Department", "Family", "FruitRegion", "Fruit", "Region", "TypePlant"]