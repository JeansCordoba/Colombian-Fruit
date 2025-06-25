from ..models import Fruit, Region, TypePlant, Family, FruitRegion, Department
from ..db import get_session

def Seed():
    with get_session() as session:
        # Seed Regions
        regions = [
            Region(name= "Andina", weather= "Templado", altitude= 2500),
            Region(name= "Caribe", weather= "Tropical seco", altitude= 200),
            Region(name= "Pacifico", weather= "Tropical húmedo", altitude= 100),
            Region(name= "Orinoquia", weather= "Tropical sabana", altitude= 200),
            Region(name= "Amazonía", weather= "Tropical húmedo", altitude= 180),
            Region(name= "Insular", weather= "Tropical seco", altitude= 10)
        ]
        session.add_all(regions)
        session.commit()
        # Seed Departments
        departments = [
            # Region Andina
            Department(name= "Antioquia", region_id= 1),
            Department(name= "Bogotá", region_id= 1),
            Department(name= "Boyacá", region_id= 1),
            Department(name= "Caldas", region_id= 1),
            Department(name= "Cundinamarca", region_id= 1),
            Department(name= "Huila", region_id= 1),
            Department(name= "Norte de Santander", region_id= 1),
            Department(name= "Quindío", region_id= 1),
            Department(name= "Risaralda", region_id= 1),
            Department(name= "Santander", region_id= 1),
            Department(name= "Tolima", region_id= 1),
            Department(name= "Cauca", region_id= 1),
            Department(name= "Nariño", region_id= 1),
            # Region Caribe
            Department(name= "Atlántico", region_id= 2),
            Department(name= "Bolívar", region_id= 2),
            Department(name= "Cesar", region_id= 2),
            Department(name= "Córdoba", region_id= 2),
            Department(name= "La Guajira", region_id= 2),
            Department(name= "Magdalena", region_id= 2),
            Department(name= "Sucre", region_id= 2),
            # Region Pacifico
            Department(name= "Chocó", region_id= 3),
            Department(name= "Córdoba", region_id= 3),
            Department(name= "Valle del Cauca", region_id= 3),
            # Region Orinoquia
            Department(name= "Arauca", region_id= 4),
            Department(name= "Casanare", region_id= 4),
            Department(name= "Meta", region_id= 4),
            Department(name= "Vichada", region_id= 4),
            # Region Amazonía
            Department(name= "Amazonas", region_id= 5),
            Department(name= "Caquetá", region_id= 5),
            Department(name= "Guaviare", region_id= 5),
            Department(name= "Guainía", region_id= 5),
            Department(name= "Vaupés", region_id= 5),
            Department(name= "Putumayo", region_id= 5),
            # Region Insular
            Department(name= "San Andrés y Providencia", region_id= 6)
        ]
        session.add_all(departments)
        session.commit()
        # Seed Type Plants
        type_plants = [
            TypePlant(name= "Árbol"),
            TypePlant(name= "Arbusto"),
            TypePlant(name= "Hierba"),
            TypePlant(name= "Enredadera"),
            TypePlant(name= "Palma"),
            TypePlant(name= "Cactus")
        ]
        session.add_all(type_plants)
        session.commit()
        # Seed Families
        families = [
            Family(name= "Rosaceae", type_plant_id= 1, description="Familia de plantas que incluye muchos árboles frutales de clima templado. Se reconocen por sus flores con 5 pétalos y hojas que crecen de forma alternada en las ramas."),
            Family(name= "Rutaceae", type_plant_id= 1, description="Familia de plantas conocidas por sus aceites aromáticos. Son árboles que mantienen sus hojas todo el año y crecen principalmente en climas cálidos."),
            Family(name= "Musaceae", type_plant_id= 3, description="Familia de plantas herbáceas muy grandes que parecen árboles. Tienen hojas enormes y crecen principalmente en climas tropicales."),
            Family(name= "Anacardiaceae", type_plant_id= 1, description="Familia de árboles que producen resinas y aceites. Tienen hojas compuestas y crecen en climas cálidos."),
            Family(name= "Solanaceae", type_plant_id= 3, description="Familia de plantas con flores en forma de estrella. Pueden ser hierbas o pequeños arbustos, y muchas tienen propiedades medicinales."),
            Family(name= "Cucurbitaceae", type_plant_id= 4, description="Familia de plantas trepadoras que se enredan en otras plantas o estructuras. Tienen tallos con forma angular y hojas grandes."),
            Family(name= "Enredadereae", type_plant_id= 2, description="Familia de plantas trepadoras con flores muy llamativas y complejas. Se enredan alrededor de otras plantas para crecer hacia arriba."),
            Family(name= "Moraceae", type_plant_id= 1, description="Familia de árboles que producen una sustancia lechosa llamada látex. Tienen hojas que crecen de forma alternada y flores pequeñas."),
            Family(name= "Lauraceae", type_plant_id= 1, description="Familia de árboles aromáticos con hojas duras y brillantes. Muchas especies se usan como especias en la cocina."),
            Family(name= "Myrtaceae", type_plant_id= 1, description="Familia de árboles y arbustos con hojas aromáticas. Tienen flores vistosas con muchos estambres y crecen en climas cálidos."),
            Family(name= "Cactaceae", type_plant_id= 6, description="Familia de plantas suculentas que almacenan agua en sus tallos. Tienen espinas en lugar de hojas y crecen en lugares secos."),
            Family(name= "Arecaceae", type_plant_id= 5, description="Familia de palmas, plantas con troncos altos sin ramas. Tienen hojas grandes en forma de abanico o pluma en la parte superior.")
        ]
        session.add_all(families)
        session.commit()
        # Seed Fruits
        fruits = [
            # 1. Rosaceae (family_id=1)
            Fruit(common_name="Manzana", scientific_name="Malus domestica", family_id=1, season="Invierno", description="Fruta de color rojo, sabor dulce y textura crujiente."),
            Fruit(common_name="Pera", scientific_name="Pyrus communis", family_id=1, season="Invierno", description="Fruta de color verde, sabor dulce y textura jugosa."),
            Fruit(common_name="Cereza", scientific_name="Prunus avium", family_id=1, season="Verano", description="Fruta pequeña, roja y dulce."),
            Fruit(common_name="Ciruela", scientific_name="Prunus domestica", family_id=1, season="Verano", description="Fruta de color morado o amarillo, sabor dulce o ácido."),
            Fruit(common_name="Durazno", scientific_name="Prunus persica", family_id=1, season="Verano", description="Fruta de piel aterciopelada y pulpa jugosa."),

            # 2. Rutaceae (family_id=2)
            Fruit(common_name="Naranja", scientific_name="Citrus sinensis", family_id=2, season="Invierno", description="Fruta cítrica de color naranja, jugosa y dulce."),
            Fruit(common_name="Limón", scientific_name="Citrus limon", family_id=2, season="Todo el año", description="Fruta cítrica de sabor ácido."),
            Fruit(common_name="Mandarina", scientific_name="Citrus reticulata", family_id=2, season="Invierno", description="Fruta cítrica pequeña, fácil de pelar."),
            Fruit(common_name="Pomelo", scientific_name="Citrus paradisi", family_id=2, season="Invierno", description="Fruta cítrica grande y ácida."),
            Fruit(common_name="Lima", scientific_name="Citrus aurantiifolia", family_id=2, season="Verano", description="Fruta cítrica pequeña y muy ácida."),

            # 3. Musaceae (family_id=3)
            Fruit(common_name="Banano", scientific_name="Musa paradisiaca", family_id=3, season="Todo el año", description="Fruta alargada, amarilla y dulce."),
            Fruit(common_name="Plátano", scientific_name="Musa acuminata", family_id=3, season="Todo el año", description="Fruta similar al banano, usada en cocina."),

            # 4. Anacardiaceae (family_id=4)
            Fruit(common_name="Mango", scientific_name="Mangifera indica", family_id=4, season="Verano", description="Fruta tropical, jugosa y dulce."),
            Fruit(common_name="Marañón", scientific_name="Anacardium occidentale", family_id=4, season="Verano", description="Fruta con nuez comestible (anacardo)."),

            # 5. Solanaceae (family_id=5)
            Fruit(common_name="Tomate", scientific_name="Solanum lycopersicum", family_id=5, season="Verano", description="Fruta roja, jugosa, usada como vegetal."),
            Fruit(common_name="Uchuva", scientific_name="Physalis peruviana", family_id=5, season="Todo el año", description="Fruta pequeña, amarilla y ácida."),
            Fruit(common_name="Berenjena", scientific_name="Solanum melongena", family_id=5, season="Verano", description="Fruta morada, usada en cocina."),

            # 6. Cucurbitaceae (family_id=6)
            Fruit(common_name="Sandía", scientific_name="Citrullus lanatus", family_id=6, season="Verano", description="Fruta grande, verde por fuera y roja por dentro."),
            Fruit(common_name="Melón", scientific_name="Cucumis melo", family_id=6, season="Verano", description="Fruta dulce, de pulpa anaranjada o verde."),
            Fruit(common_name="Pepino", scientific_name="Cucumis sativus", family_id=6, season="Verano", description="Fruta alargada, verde, usada como vegetal."),
            Fruit(common_name="Calabaza", scientific_name="Cucurbita pepo", family_id=6, season="Otoño", description="Fruta grande, naranja, usada en cocina."),

            # 7. Enredadereae (family_id=7)
            Fruit(common_name="Maracuyá", scientific_name="Passiflora edulis", family_id=7, season="Verano", description="Fruta tropical, ácida y aromática."),
            Fruit(common_name="Granadilla", scientific_name="Passiflora ligularis", family_id=7, season="Verano", description="Fruta dulce, de pulpa gelatinosa."),

            # 8. Moraceae (family_id=8)
            Fruit(common_name="Higo", scientific_name="Ficus carica", family_id=8, season="Verano", description="Fruta pequeña, dulce y morada."),
            Fruit(common_name="Jaca", scientific_name="Artocarpus heterophyllus", family_id=8, season="Verano", description="Fruta grande, tropical y dulce."),

            # 9. Lauraceae (family_id=9)
            Fruit(common_name="Aguacate", scientific_name="Persea americana", family_id=9, season="Todo el año", description="Fruta verde, cremosa y nutritiva."),

            # 10. Myrtaceae (family_id=10)
            Fruit(common_name="Guayaba", scientific_name="Psidium guajava", family_id=10, season="Verano", description="Fruta tropical, dulce y aromática."),
            Fruit(common_name="Feijoa", scientific_name="Acca sellowiana", family_id=10, season="Otoño", description="Fruta verde, dulce y ácida."),

            # 11. Cactaceae (family_id=11)
            Fruit(common_name="Nopal", scientific_name="Opuntia ficus-indica", family_id=11, season="Primavera", description="Fruto de cactus, comestible y nutritivo."),
            Fruit(common_name="Pitaya", scientific_name="Hylocereus undatus", family_id=11, season="Verano", description="Fruta exótica, rosa por fuera y blanca por dentro."),
            Fruit(common_name="Tuna", scientific_name="Opuntia", family_id=11, season="Verano", description="Fruta de cactus, dulce y refrescante."),

            # 12. Arecaceae (family_id=12)
            Fruit(common_name="Coco", scientific_name="Cocos nucifera", family_id=12, season="Verano", description="Fruta tropical, dura por fuera y blanca por dentro."),
            Fruit(common_name="Palma de aceite", scientific_name="Elaeis guineensis", family_id=12, season="Verano", description="Fruto de palma, fuente de aceite vegetal."),
            Fruit(common_name="Dátil", scientific_name="Phoenix dactylifera", family_id=12, season="Otoño", description="Fruta dulce, marrón y alargada."),
        ]
        session.add_all(fruits)
        session.commit()
        fruit_regions = [
        # Manzana (Andina)
        FruitRegion(fruit_id=1, region_id=1),
        # Pera (Andina)
        FruitRegion(fruit_id=2, region_id=1),
        # Cereza (Andina)
        FruitRegion(fruit_id=3, region_id=1),
        # Ciruela (Andina, Caribe)
        FruitRegion(fruit_id=4, region_id=1),
        FruitRegion(fruit_id=4, region_id=2),
        # Durazno (Andina)
        FruitRegion(fruit_id=5, region_id=1),

        # Naranja (Andina, Caribe, Pacifico)
        FruitRegion(fruit_id=6, region_id=1),
        FruitRegion(fruit_id=6, region_id=2),
        FruitRegion(fruit_id=6, region_id=3),
        # Limón (Caribe, Pacifico)
        FruitRegion(fruit_id=7, region_id=2),
        FruitRegion(fruit_id=7, region_id=3),
        # Mandarina (Andina, Caribe)
        FruitRegion(fruit_id=8, region_id=1),
        FruitRegion(fruit_id=8, region_id=2),
        # Pomelo (Caribe)
        FruitRegion(fruit_id=9, region_id=2),
        # Lima (Caribe)
        FruitRegion(fruit_id=10, region_id=2),

        # Banano (Caribe, Pacifico, Amazonía)
        FruitRegion(fruit_id=11, region_id=2),
        FruitRegion(fruit_id=11, region_id=3),
        FruitRegion(fruit_id=11, region_id=5),
        # Plátano (Andina, Caribe)
        FruitRegion(fruit_id=12, region_id=1),
        FruitRegion(fruit_id=12, region_id=2),

        # Mango (Caribe, Orinoquia)
        FruitRegion(fruit_id=13, region_id=2),
        FruitRegion(fruit_id=13, region_id=4),
        # Marañón (Caribe)
        FruitRegion(fruit_id=14, region_id=2),

        # Tomate (Andina, Caribe)
        FruitRegion(fruit_id=15, region_id=1),
        FruitRegion(fruit_id=15, region_id=2),
        # Uchuva (Andina)
        FruitRegion(fruit_id=16, region_id=1),
        # Berenjena (Caribe)
        FruitRegion(fruit_id=17, region_id=2),

        # Sandía (Caribe, Orinoquia)
        FruitRegion(fruit_id=18, region_id=2),
        FruitRegion(fruit_id=18, region_id=4),
        # Melón (Caribe, Orinoquia)
        FruitRegion(fruit_id=19, region_id=2),
        FruitRegion(fruit_id=19, region_id=4),
        # Pepino (Andina)
        FruitRegion(fruit_id=20, region_id=1),
        # Calabaza (Caribe)
        FruitRegion(fruit_id=21, region_id=2),

        # Maracuyá (Andina, Amazonía)
        FruitRegion(fruit_id=22, region_id=1),
        FruitRegion(fruit_id=22, region_id=5),
        # Granadilla (Andina)
        FruitRegion(fruit_id=23, region_id=1),

        # Higo (Andina)
        FruitRegion(fruit_id=24, region_id=1),
        # Jaca (Amazonía)
        FruitRegion(fruit_id=25, region_id=5),

        # Aguacate (Andina, Caribe, Pacifico)
        FruitRegion(fruit_id=26, region_id=1),
        FruitRegion(fruit_id=26, region_id=2),
        FruitRegion(fruit_id=26, region_id=3),

        # Guayaba (Andina, Caribe)
        FruitRegion(fruit_id=27, region_id=1),
        FruitRegion(fruit_id=27, region_id=2),
        # Feijoa (Andina)
        FruitRegion(fruit_id=28, region_id=1),

        # Nopal (Caribe)
        FruitRegion(fruit_id=29, region_id=2),
        # Pitaya (Andina, Caribe)
        FruitRegion(fruit_id=30, region_id=1),
        FruitRegion(fruit_id=30, region_id=2),
        # Tuna (Andina)
        FruitRegion(fruit_id=31, region_id=1),

        # Coco (Caribe, Pacifico, Insular)
        FruitRegion(fruit_id=32, region_id=2),
        FruitRegion(fruit_id=32, region_id=3),
        FruitRegion(fruit_id=32, region_id=6),
        # Palma de aceite (Caribe, Pacifico)
        FruitRegion(fruit_id=33, region_id=2),
        FruitRegion(fruit_id=33, region_id=3),
        # Dátil (Caribe)
        FruitRegion(fruit_id=34, region_id=2),
    ]
    session.add_all(fruit_regions)
    session.commit()

if __name__ == "__main__":
    Seed()    
    print("Seed completed")
