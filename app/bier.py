from fastapi import FastAPI
from pydantic import BaseModel


# class voor item
class Bier(BaseModel):
    naam: str
    volume: int
    alcohol_perc: float
    brouwerij: str
    soort: str
    land: str


# opstarten van api
app = FastAPI()

# lijst
bieren = []

# database voor basic program
database = [
    {"naam": "Westmalle extra", "volume": "33", "alcohol_perc": "4.8", "brouwerij": "Westmalle", "soort": "blond",
     "land": "België"},
    {"naam": "Westmalle triple", "volume": "33", "alcohol_perc": "9.5", "brouwerij": "Westmalle", "soort": "triple",
     "land": "België"},
    {"naam": "Westmalle dubbel", "volume": "33", "alcohol_perc": "7", "brouwerij": "Westmalle", "soort": "dubbel",
     "land": "België"}]

# items van database doorlopen en in lijst zetten
for item in database:
    nieuw_bier = Bier(naam=item["naam"], volume=item["volume"], alcohol_perc=item["alcohol_perc"],
                      brouwerij=item["brouwerij"], soort=item["soort"], land=item["land"])
    bieren.append(nieuw_bier)


# get bieren
@app.get("/bier")
async def get_bieren():
    return bieren


# get bieren van bepaalde brouwerij
@app.get("/brouwerij/{brouwerij}")
async def get_brouwerij(*, brouwerij: str):
    # lijst voor de brouwerij
    bieren_brouwerij = []
    # bieren overlopen
    for bier in bieren:
        # als de naam matcht
        if bier.brouwerij == name:
            # deel van class gebruiken
            bieren_brouwerij.append(bier.naam)
    return bieren_brouwerij


# get bieren per soort
@app.get("/soort")
async def get_soort():
    keys = []
    soorten = {}
    for bier in bieren:
        if bier.soort not in keys:
            keys.append(bier.soort)

    for i in range(len(keys)):
        bieren_per_soort = []
        for bier in bieren:
            if bier.soort == keys[i]:
                bieren_per_soort.append(bier)
        soorten[keys[i]] = bieren_per_soort

    return soorten


@app.post("/bier/", response_model=Bier)
async def create_bier(bier: Bier):
    return bier

