
import requests
from dotenv import load_dotenv
import os

API_URL = "https://router.huggingface.co/v1/chat/completions"
load_dotenv()

API_KEY = os.getenv("HF_API_KEY")
headers = {
    "Authorization": f"Bearer {API_KEY}",
}

def gerar_resposta_api(texto):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"gere uma mensagem curta, seria e profissional respondendo ao texto {texto}" if texto == 'Produtivo' else f'gere uma mensagem curta e gentil respondendo ao {texto}'
            }
        ],
        "model": "moonshotai/Kimi-K2-Thinking"
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    return data["choices"][0]["message"]["content"] if "choices" in data else "Erro na geração da resposta"

