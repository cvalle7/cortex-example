from fastapi import APIRouter, HTTPException
from app.models.cortex_mode import Cortex_data
from app.services.cortex_service import get_chat

router = APIRouter()

@router.get('/hello')
def hello():
    return {"message": "hello"}

@router.post('/chat')
def chat(data: Cortex_data):
    try:
        message = get_chat(data.message)
        return {"data": message.choices.message.content}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=f"Error, {error}")
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Internal Server Error, {error}")