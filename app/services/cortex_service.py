import requests
from dotenv import load_dotenv
import os

load_dotenv()

host=os.getenv('CORTEX_HOST')
port=os.getenv('CORTEX_PORT')
model = "llama3.1:8b-gguf-q4-ks"
url = f"http://{host}:{port}/v1/chat/completions"

async def get_chat(message: str):

    payload = {
        "messages": [
            {
                "content": message,
                "role": "user"
            }
        ],
        "model": "mistral",
        "stream": True,
        "max_tokens": 4096,
        "stop": ["End"],
        "frequency_penalty": 0.2,
        "presence_penalty": 0.6,
        "temperature": 0.8,
        "top_p": 0.95
    }

    headers = {"Content-Type": "application/json"}
    
    response = await requests.post(url, json=payload, headers=headers)
    
    return response.json()
