# Colombian Fruits API

Proyecto personal de estudio que busca contribuir a la comunidad colombiana proporcionando información detallada sobre el origen geográfico y botánico de las frutas del país. Esta API permite explorar dónde se cultivan las frutas colombianas, a qué familias botánicas pertenecen y en qué regiones y departamentos se encuentran, facilitando el conocimiento y aprecio por la biodiversidad frutícola nacional.

## Estado del Proyecto

**DESARROLLO ACTIVO - NO RECOMENDADO PARA PRODUCCIÓN**

Este proyecto está en desarrollo activo y puede experimentar cambios significativos:
- Endpoints y estructura pueden cambiar
- Modelos de datos pueden ser modificados
- Funcionalidades pueden ser agregadas o eliminadas
- La documentación puede quedar desactualizada temporalmente

### Completado
- ✅ Estructura del proyecto y arquitectura en capas
- ✅ Modelos de datos con relaciones
- ✅ Endpoints básicos implementados
- ✅ Base de datos semilla con datos reales
- ✅ Configuración Docker funcional
- ✅ Serialización de respuestas corregida
- ✅ Refactorización completa del backend
- ✅ Documentación mejorada

### Pendiente
- **Autenticación y autorización** (JWT)
- **Pruebas unitarias** en todas las capas
- **Pruebas de integración** para endpoints
- **Validación de datos** mejorada
- **Documentación de API** completa
- **Optimización de consultas** de base de datos
- **Frontend** para consumir la API
- **Logging y middleware** de errores

## Características

- **API RESTful** con FastAPI y SQLModel
- **Base de datos PostgreSQL** con datos semilla de frutas colombianas
- **Arquitectura en capas**: Models, Schemas, Services, Routes
- **Docker** para containerización
- **38 endpoints** implementados para gestión completa de datos
- **Relaciones complejas** entre frutas, regiones, departamentos, familias y tipos de planta
- **Búsquedas avanzadas** con filtros por nombre y descripción
- **Respuestas detalladas** con información relacionada
- **Alto rendimiento** y escalabilidad

## Próximos Pasos

### Prioridad Alta
1. **Implementar autenticación JWT**
   - Crear sistema de usuarios y roles
   - Proteger endpoints sensibles (POST, PATCH, DELETE)
   - Implementar middleware de autenticación

2. **Desarrollar pruebas completas**
   - Pruebas unitarias para modelos
   - Pruebas unitarias para servicios
   - Pruebas de integración para endpoints

### Prioridad Media
3. **Implementar logging y middleware**
   - Logging estructurado para debugging
   - Middleware para manejo global de errores
   - Monitoreo de performance

4. **Desarrollar frontend**
   - Interfaz de usuario para consumir la API
   - Dashboard de administración
   - Visualización de datos

### Prioridad Baja
5. **Optimizar rendimiento**
   - Optimizar consultas de base de datos
   - Implementar paginación
   - Agregar índices a la base de datos

6. **Documentación y despliegue**
   - Documentación completa de API
   - Guías de despliegue
   - Monitoreo y métricas

7. **Configurar CI/CD**
   - Configurar GitHub Actions para ejecutar pruebas
   - Automatizar despliegue
   - Integración continua

## Tabla de Contenidos

- [Tecnologías](#tecnologías)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)
- [Modelos de Datos](#modelos-de-datos)
- [Características Avanzadas](#características-avanzadas)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Tecnologías

### Backend
- **FastAPI** - Framework web moderno y rápido
- **SQLModel** - ORM moderno basado en SQLAlchemy y Pydantic
- **PostgreSQL** - Base de datos relacional robusta
- **Pydantic** - Validación de datos y serialización
- **Uvicorn** - Servidor ASGI de alto rendimiento

### DevOps
- **Docker** - Containerización
- **Docker Compose** - Orquestación de servicios
- **Python 3.11+** - Lenguaje de programación

## Estructura del Proyecto

```
Colombian_fruits/
├── src/
│   ├── backend/
│   │   ├── app/
│   │   │   ├── models/          # Modelos de base de datos
│   │   │   ├── schemas/         # Esquemas Pydantic
│   │   │   ├── services/        # Lógica de negocio
│   │   │   ├── routes/          # Endpoints de la API
│   │   │   ├── db/              # Configuración de BD
│   │   │   ├── utilities/       # Utilidades y helpers
│   │   │   └── auth/            # Autenticación (preparado)
│   │   ├── tests/               # Pruebas unitarias e integración
│   │   │   ├── test_models/     # Pruebas de modelos
│   │   │   ├── test_services/   # Pruebas de servicios
│   │   │   └── test_routes/     # Pruebas de rutas
│   │   ├── env/                 # Entorno virtual Python
│   │   ├── requirements.txt     # Dependencias Python
│   │   ├── Dockerfile          # Configuración Docker
│   │   └── main.py             # Punto de entrada
│   └── frontend/               # Frontend (vacío - futuro)
├── docker-compose.yml          # Orquestación de servicios
├── .env                        # Variables de entorno (crear)
├── .gitignore                  # Archivos ignorados por Git
├── LICENSE                     # Licencia del proyecto
└── README.md                   # Este archivo
```

## Instalación

### Prerrequisitos
- Docker y Docker Compose
- Git

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/JeansCordoba/Colombian-Fruit
cd Colombian_fruits
```

2. **Configurar variables de entorno**
```bash
# Crear archivo .env en la raíz del proyecto
touch .env
```

3. **Agregar variables al archivo .env**
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=colombian_fruits_db
POSTGRES_HOST=colombian-fruits-db
```

4. **Ejecutar con Docker Compose**
```bash
docker-compose up -d
```

5. **Verificar que todo funcione**
```bash
# La API estará disponible en: http://localhost:8000
# La documentación en: http://localhost:8000/docs
```

## Configuración

### Variables de Entorno (.env)
```env
# Variables para la base de datos PostgreSQL
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=colombian_fruits_db
POSTGRES_HOST=colombian-fruits-db
```

## Uso

### Iniciar el proyecto
```bash
# Desarrollo
docker-compose up --build

# Ver logs
docker-compose logs -f api-colombian-fruits

# Detener
docker-compose stop
```

### Acceder a la documentación
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Poblar la Base de Datos
Para cargar datos de ejemplo en la base de datos:

```bash
# Ejecutar el seed desde dentro del contenedor
docker-compose exec api-colombian-fruits python -m app.utilities.seed
```

**Nota**: El seed incluye datos reales de frutas colombianas, regiones, departamentos y familias botánicas.

## API Endpoints

**Total: 38 endpoints implementados**

### Frutas (Fruits) - 7 endpoints
- `POST /api/v1/fruits/` - Crear fruta
- `GET /api/v1/fruits/` - Listar todas las frutas
- `GET /api/v1/fruits/{fruit_id}` - Obtener fruta por ID
- `GET /api/v1/fruits/regions/{fruit_id}` - Obtener regiones de una fruta
- `GET /api/v1/fruits/search` - Buscar frutas
- `PATCH /api/v1/fruits/{fruit_id}` - Actualizar fruta
- `DELETE /api/v1/fruits/{fruit_id}` - Eliminar fruta

### Regiones (Regions) - 7 endpoints
- `POST /api/v1/regions/` - Crear región
- `GET /api/v1/regions/` - Listar todas las regiones
- `GET /api/v1/regions/{region_id}` - Obtener región por ID
- `GET /api/v1/regions/fruits/{region_id}` - Obtener frutas de una región
- `GET /api/v1/regions/search` - Buscar regiones
- `PATCH /api/v1/regions/{region_id}` - Actualizar región
- `DELETE /api/v1/regions/{region_id}` - Eliminar región

### Departamentos (Departments) - 7 endpoints
- `POST /api/v1/departments/` - Crear departamento
- `GET /api/v1/departments/` - Listar todos los departamentos
- `GET /api/v1/departments/{department_id}` - Obtener departamento por ID
- `GET /api/v1/departments/search` - Buscar departamentos
- `PATCH /api/v1/departments/{department_id}` - Actualizar departamento
- `DELETE /api/v1/departments/{department_id}` - Eliminar departamento

### Familias (Families) - 7 endpoints
- `POST /api/v1/families/` - Crear familia
- `GET /api/v1/families/` - Listar todas las familias
- `GET /api/v1/families/{family_id}` - Obtener familia por ID
- `GET /api/v1/families/search` - Buscar familias
- `PATCH /api/v1/families/{family_id}` - Actualizar familia
- `DELETE /api/v1/families/{family_id}` - Eliminar familia

### Tipos de Planta (Type Plants) - 7 endpoints
- `POST /api/v1/type-plants/` - Crear tipo de planta
- `GET /api/v1/type-plants/` - Listar todos los tipos
- `GET /api/v1/type-plants/{type_plant_id}` - Obtener tipo por ID
- `GET /api/v1/type-plants/search` - Buscar tipos
- `PATCH /api/v1/type-plants/{type_plant_id}` - Actualizar tipo
- `DELETE /api/v1/type-plants/{type_plant_id}` - Eliminar tipo

### Relaciones Fruta-Región - 3 endpoints
- `POST /api/v1/fruit-regions/` - Crear relación fruta-región
- `GET /api/v1/fruit-regions/` - Listar todas las relaciones
- `DELETE /api/v1/fruit-regions/{fruit_id}/{region_id}` - Eliminar relación fruta-región

## Modelos de Datos

### Entidades Principales
- **Fruit**: Frutas con nombre común, científico, familia, temporada y descripción
- **Region**: Regiones geográficas de Colombia con clima y altitud
- **Department**: Departamentos de Colombia
- **Family**: Familias botánicas con descripción
- **TypePlant**: Tipos de plantas (árbol, arbusto, etc.)

### Relaciones
- **Fruit ↔ Region**: Muchos-a-muchos (a través de FruitRegion)
- **Department → Region**: Muchos-a-uno
- **Fruit → Family**: Muchos-a-uno
- **Family → TypePlant**: Muchos-a-uno

## Características Avanzadas

### Búsquedas Inteligentes
- Búsqueda por texto con filtros `ILIKE`
- Filtros múltiples combinados
- Búsqueda por relaciones (ej: frutas por región)
- Validación de acentos y mayúsculas/minúsculas

### Validaciones
- Campos requeridos y opcionales
- Validación de longitudes de texto
- Verificación de existencia de entidades relacionadas
- Prevención de duplicados con normalización

### Respuestas Flexibles
- Múltiples formatos de respuesta según el endpoint
- Serialización automática de relaciones
- Configuración de campos extra (ignore/forbid)

### Funcionalidades Especiales
- Gestión completa de frutas colombianas
- Mapeo de regiones y departamentos
- Clasificación botánica por familias
- Relaciones fruta-región para análisis geográfico

## Contribución

**Proyecto en Desarrollo Activo**

Este proyecto está en constante evolución. Si quieres contribuir:

1. **Comunícate** antes de hacer cambios grandes
2. **Mantén la documentación actualizada** con tus cambios

### Proceso de Contribución
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guías de Contribución
- Sigue las convenciones de código existentes
- Agrega tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario
- Verifica que todos los tests pasen
- **Comunica cambios importantes** en la estructura o endpoints

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

- **Autor**: Jeans Carlos Asprilla Córdoba
- **Email**: jeans.carlos.asprilla@gmail.com
- **Proyecto**: Colombian Fruits API - Estudio personal sobre biodiversidad frutícola colombiana

---

⭐ Si este proyecto te ha sido útil, ¡dale una estrella en GitHub!

## Estado de Pruebas

**IMPORTANTE**: Aunque todos los endpoints están implementados, **NO han sido probados exhaustivamente**. Se recomienda:

- **Probar cada endpoint** antes de usar en producción
- **Verificar respuestas** y códigos de estado HTTP
- **Validar datos** de entrada y salida
- **Crear pruebas automatizadas** para garantizar funcionamiento

**Próximo paso recomendado**: Implementar pruebas unitarias y de integración para todos los endpoints.
