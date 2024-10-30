from fastapi import APIRouter
from app.models.cortex_mode import Cortex_data
from app.services.cortex_service import get_chat

router = APIRouter()

@router.get('/hello')
async def hello():
    return {"message": "hello"}

@router.post('/chat')
async def chat(data: Cortex_data):
    message = await get_chat(data)
    return {"message": "This is a post", "data": message}