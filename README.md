# 🍎 Colombian Fruits API

Proyecto personal de estudio que busca contribuir a la comunidad colombiana proporcionando información detallada sobre el origen geográfico y botánico de las frutas del país. Esta API permite explorar dónde se cultivan las frutas colombianas, a qué familias botánicas pertenecen y en qué regiones y departamentos se encuentran, facilitando el conocimiento y aprecio por la biodiversidad frutícola nacional.

## ⚠️ Estado del Proyecto - IMPORTANTE

**🚧 DESARROLLO ACTIVO - CAMBIOS FRECUENTES**

Este proyecto está **en desarrollo activo** y es muy probable que experimente cambios significativos:

- **Endpoints**: La estructura y lógica de los endpoints puede cambiar
- **Modelos de datos**: Los esquemas y relaciones pueden ser modificados
- **Funcionalidades**: Se pueden agregar, eliminar o reestructurar características
- **Base de datos**: La estructura de tablas puede evolucionar

**⚠️ ADVERTENCIA**: 
- Esta API no está desplegada públicamente
- **NO se recomienda para uso en producción**
- Úsala solo para fines de estudio y contribución al desarrollo
- La documentación puede quedar desactualizada temporalmente

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [API Endpoints](#-api-endpoints)
- [Modelos de Datos](#-modelos-de-datos)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

## ✨ Características

- **API REST completa** con FastAPI
- **Base de datos PostgreSQL** con SQLModel/SQLAlchemy
- **Validación de datos** con Pydantic
- **Documentación automática** con Swagger/OpenAPI
- **Docker y Docker Compose** para fácil despliegue
- **Arquitectura limpia** con separación de responsabilidades
- **Relaciones complejas** entre entidades (muchos-a-muchos)
- **Búsquedas avanzadas** con filtros múltiples
- **Validaciones personalizadas** (acentos, duplicados, etc.)

## 🛠 Tecnologías

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

## 📁 Estructura del Proyecto

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
│   │   │   └── utilities/       # Utilidades y helpers
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

## 🚀 Instalación

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
POSTGRES_USER=colombian_fruits
POSTGRES_PASSWORD=your_password
POSTGRES_DB=colombian_fruits_db
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

## ⚙️ Configuración

### Variables de Entorno (.env)
```env
# Base de datos
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=colombian_fruits_db
POSTGRES_HOST=database
```

## 📖 Uso

### Iniciar el proyecto
```bash
# Desarrollo
docker-compose up -d

# Ver logs
docker-compose logs -f api-colombian-fruits

# Detener
docker-compose down
```

### Acceder a la documentación
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🔌 API Endpoints

**📝 Nota**: Los endpoints documentados corresponden a la versión actual del proyecto. Debido al desarrollo activo, pueden cambiar en futuras versiones.

### Frutas (Fruits)
- `GET /api/v1/fruits/` - Obtener todas las frutas
- `GET /api/v1/fruits/{fruit_id}` - Obtener fruta por ID
- `POST /api/v1/fruits/` - Crear nueva fruta
- `PATCH /api/v1/fruits/{fruit_id}` - Actualizar fruta
- `DELETE /api/v1/fruits/{fruit_id}` - Eliminar fruta
- `GET /api/v1/fruits/search` - Buscar frutas

### Departamentos (Departments)
- `GET /api/v1/departments/` - Obtener todos los departamentos
- `GET /api/v1/departments/detail` - Obtener departamentos con detalles
- `GET /api/v1/departments/{department_id}` - Obtener departamento por ID
- `GET /api/v1/departments/detail/{department_id}` - Obtener departamento con detalles por ID
- `POST /api/v1/departments/` - Crear nuevo departamento
- `PATCH /api/v1/departments/{department_id}` - Actualizar departamento
- `DELETE /api/v1/departments/{department_id}` - Eliminar departamento
- `GET /api/v1/departments/search` - Buscar departamentos
- `GET /api/v1/departments/search/detail` - Buscar departamentos con detalles

### Regiones (Regions)
- `GET /api/v1/regions/` - Obtener todas las regiones
- `GET /api/v1/regions/{region_id}` - Obtener región por ID
- `POST /api/v1/regions/` - Crear nueva región
- `PATCH /api/v1/regions/{region_id}` - Actualizar región
- `DELETE /api/v1/regions/{region_id}` - Eliminar región
- `GET /api/v1/regions/search` - Buscar regiones

### Familias (Families)
- `GET /api/v1/families/` - Obtener todas las familias
- `GET /api/v1/families/{family_id}` - Obtener familia por ID
- `POST /api/v1/families/` - Crear nueva familia
- `PATCH /api/v1/families/{family_id}` - Actualizar familia
- `DELETE /api/v1/families/{family_id}` - Eliminar familia
- `GET /api/v1/families/search` - Buscar familias

### Tipos de Planta (Type Plants)
- `GET /api/v1/type-plants/` - Obtener todos los tipos de planta
- `GET /api/v1/type-plants/{type_plant_id}` - Obtener tipo de planta por ID
- `POST /api/v1/type-plants/` - Crear nuevo tipo de planta
- `PATCH /api/v1/type-plants/{type_plant_id}` - Actualizar tipo de planta
- `DELETE /api/v1/type-plants/{type_plant_id}` - Eliminar tipo de planta
- `GET /api/v1/type-plants/search` - Buscar tipos de planta

### Relaciones Fruta-Región (Fruit-Region)
- `POST /api/v1/fruit-regions/` - Crear relación fruta-región
- `DELETE /api/v1/fruit-regions/?fruit_id={fruit_id}&region_id={region_id}` - Eliminar relación fruta-región

## 🗄️ Modelos de Datos

**📝 Nota**: Los modelos de datos pueden evolucionar durante el desarrollo. Consulta la documentación de la API para la versión más actualizada.

### Entidades Principales
- **Fruit**: Frutas con nombre común, científico, familia, temporada
- **Region**: Regiones geográficas de Colombia
- **Department**: Departamentos de Colombia
- **Family**: Familias botánicas
- **TypePlant**: Tipos de plantas (árbol, arbusto, etc.)

### Relaciones
- **Fruit ↔ Region**: Muchos-a-muchos (a través de FruitRegion)
- **Department → Region**: Muchos-a-uno
- **Fruit → Family**: Muchos-a-uno
- **Family → TypePlant**: Muchos-a-uno

## 🔍 Características Avanzadas

### Búsquedas Inteligentes
- Búsqueda por texto con `ILIKE`
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

## 🤝 Contribución

**🚧 Proyecto en Desarrollo Activo**

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

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Contacto

- **Autor**: Jeans Carlos Asprilla Córdoba
- **Email**: jeans.carlos.asprilla@gmail.com
- **Proyecto**: Colombian Fruits API - Estudio personal sobre biodiversidad frutícola colombiana

---

⭐ Si este proyecto te ha sido útil, ¡dale una estrella en GitHub!
