import requests
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('CORTEX_HOST')
port = os.getenv('CORTEX_PORT')
model = "llama3.1:8b-gguf-q4-ks"
headers = {"Content-Type": "application/json"}


def start_model():
    url = f"http://{host}:{port}/v1/models/start"

    payload = {
        "model": model,
        "prompt_template": "system\n{system_message}\nuser\n{prompt}\nassistant",
        "stop": [],
        "ngl": 4096,
        "ctx_len": 4096,
        "cpu_threads": 10,
        "n_batch": 2048,
        "caching_enabled": True,
        "grp_attn_n": 1,
        "grp_attn_w": 512,
        "mlock": False,
        "flash_attn": True,
        "cache_type": "f16",
        "use_mmap": True,
        "engine": "llama-cpp"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def stop_model():
    url = f"http://{host}:{port}/v1/models/stop"
    
    payload = {
        "model": model
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def get_chat(message: str):

    url = f"http://{host}:{port}/v1/chat/completions"

    payload = {
        "messages": [
            {
                "content": message,
                "role": "user"
            }
        ],
        "model": model,
        "stream": False,
        "max_tokens": 4096,
        "stop": ["End"],
        "frequency_penalty": 0.2,
        "presence_penalty": 0.6,
        "temperature": 0.8,
        "top_p": 0.95
    }

    response = requests.post(url, json=payload, headers=headers)
    content = response.json()['choices'][0]['message']['content']

    return content
