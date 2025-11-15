import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://router.huggingface.co/hf-inference/models/joeddav/xlm-roberta-large-xnli"
headers = {
    "Authorization": f"Bearer {API_KEY}",
}



def classify_email(text):
    text = text.lower()

    keywords_productive = [
        'ajuda', 'suporte', 'erro', 'problema', 'solicitação',
        'atualização', 'cliente', 'urgente', 'demora', 'funcionando',
        'login', 'acesso', 'falha', 'instabilidade'
    ]

    keywords_unproductive = [
        'feliz natal', 'boa sorte', 'parabéns', 'obrigado', 'agradeço',
        'oi', 'olá', 'bom dia', 'boa tarde', 'boa noite',
        'teste', 'testando', 'quanto', 'qual', '?'
    ]

    count_prod = sum(1 for kw in keywords_productive if kw in text)
    count_unprod = sum(1 for kw in keywords_unproductive if kw in text)

    if count_prod > count_unprod:
        return "Produtivo"
    elif count_unprod > count_prod:
        return "Improdutivo"
    else:
        # fallback: modelo huggingface
    
        payload = {
        "inputs": text,
        "parameters": {
            "candidate_labels": ["produtivo", "improdutivo"]
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    if "labels" not in result:
            return "Improdutivo"

    label = result["labels"][0]

    return "Produtivo" if label == "produtivo" else "Improdutivo"

