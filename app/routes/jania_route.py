from fastapi import APIRouter, HTTPException
from app.models.cortex_mode import Cortex_data
from app.services.cortex_service import get_chat

router = APIRouter()

@router.get('/hello')
async def hello():
    return {"message": "hello"}

@router.post('/chat')
async def chat(data: Cortex_data):
    try:
        message = await get_chat(data)
        return {"message": "This is a post", "data": message}
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Internal Server Error, {error}")