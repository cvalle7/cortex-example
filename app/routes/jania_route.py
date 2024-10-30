from fastapi import APIRouter, HTTPException
from app.models.cortex_mode import Cortex_data
from app.services.cortex_service import get_chat, start_model, stop_model

router = APIRouter()

@router.get('/start')
def start():
    try:
        response = start_model()
        return {"data": response}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=f"Error, {error}")
    except Exception as error:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error, {error}")


@router.get('/stop')
def stop():
    try:
        response = stop_model()
        return {"data": response}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=f"Error, {error}")
    except Exception as error:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error, {error}")


@router.post('/chat')
def chat(data: Cortex_data):
    try:
        message = get_chat(data.message)
        return {"data": message}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=f"Error, {error}")
    except Exception as error:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error, {error}")
