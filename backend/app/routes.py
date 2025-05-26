from fastapi import APIRouter
from app.pdb_utils import fetch_and_store_protein

router = APIRouter()

@router.post("/submit_ids")
def submit_protein_ids(pdb_ids: list[str]):
    results = {}
    for pdb_id in pdb_ids:
        results[pdb_id] = fetch_and_store_protein(pdb_id)
    return results