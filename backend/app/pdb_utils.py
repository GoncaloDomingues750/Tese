import requests
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["protein_db"]

async def fetch_and_store_protein(pdb_id):
    existing = await db.proteins.find_one({"pdb_id": pdb_id})
    if existing:
        return {"status": "exists", "pdb_id": pdb_id}

    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    r = requests.get(url)
    if r.status_code == 200:
        protein_data = r.json()
        await db.proteins.insert_one({"pdb_id": pdb_id, "data": protein_data})
        return {"status": "stored", "pdb_id": pdb_id}
    return {"status": "error", "pdb_id": pdb_id}
