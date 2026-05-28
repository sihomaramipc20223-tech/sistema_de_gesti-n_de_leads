from pydantic import BaseModel

class Person(BaseModel):
    nombre: str
    genero: str
    ubicacion: str
    correo: str
    fecha_nacimiento: str
    fotografia: str

class PersonsResponse(BaseModel):
    success: bool
    data: list[Person]
    total: int