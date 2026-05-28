import httpx
from app.models.person import Person

RANDOMUSER_URL = "https://randomuser.me/api/"

async def fetch_persons(results: int = 10) -> list[Person]:
    params = {
        "results": results,
        "inc": "name,gender,location,email,dob,picture"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(RANDOMUSER_URL, params=params)
        response.raise_for_status()
        data = response.json()

    persons = []
    for p in data["results"]:
        persons.append(Person(
            nombre=f"{p['name']['first']} {p['name']['last']}",
            genero=p["gender"],
            ubicacion=f"{p['location']['city']}, {p['location']['country']}",
            correo=p["email"],
            fecha_nacimiento=p["dob"]["date"].split("T")[0],
            fotografia=p["picture"]["large"]
        ))

    return persons