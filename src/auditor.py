from fastapi import APIRouter, HTTPException
from src.clio_client import ClioClient

router = APIRouter()
client = ClioClient()

@router.get("/audit/{matter_id}")
async def audit_matter(matter_id: str):
    try:
        data = await client.get_matter(matter_id)
        # Add your business logic here
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))