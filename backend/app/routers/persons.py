from fastapi import APIRouter, HTTPException
from app.models.person import PersonsResponse
from app.services.randomuser_service import fetch_persons

router = APIRouter(prefix="/api/persons", tags=["Personas"])

@router.get(
    "/",
    response_model=PersonsResponse,
    summary="Obtener lista de personas",
    description="Retorna una lista de 10 personas con datos ficticios desde RandomUser API."
)
async def get_persons():
    try:
        persons = await fetch_persons(results=10)
        return PersonsResponse(
            success=True,
            data=persons,
            total=len(persons)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{cantidad}",
    response_model=PersonsResponse,
    summary="Obtener N personas",
    description="Retorna la cantidad especificada de personas (máximo 50)."
)
async def get_persons_by_count(cantidad: int):
    if cantidad < 1 or cantidad > 50:
        raise HTTPException(
            status_code=400,
            detail="La cantidad debe estar entre 1 y 50"
        )
    try:
        persons = await fetch_persons(results=cantidad)
        return PersonsResponse(
            success=True,
            data=persons,
            total=len(persons)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))