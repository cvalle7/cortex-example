import os
from fastapi import FastAPI
from app.routes import router
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '3333'))
    uvicorn.run("app.main:app", host=host, port=port, reload=True)