from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import persons

app = FastAPI(
    title="NTT Data - API de Personas",
    description="""
## API RESTful para gestión de personas

Genera listas de personas con datos ficticios consumiendo la **RandomUser API**.

### Datos retornados por persona:
- **Nombre** completo
- **Género**
- **Ubicación** (ciudad y país)
- **Correo electrónico**
- **Fecha de nacimiento**
- **Fotografía** (URL)
    """,
    version="1.0.0",
    contact={
        "name": "NTT Data Bootcamp",
        "url": "https://github.com/sihomaramipc20223-tech/sistema_de_gesti-n_de_leads"
    },
    license_info={
        "name": "MIT"
    }
)

# CORS — permite peticiones desde el frontend Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # En producción: poner la URL de Firebase
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(persons.router)

@app.get("/", tags=["Health"])
async def root():
    return {
        "status": "ok",
        "message": "API NTT Data corriendo correctamente",
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}