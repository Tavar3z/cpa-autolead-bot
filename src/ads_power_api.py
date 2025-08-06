import requests
from src.config import API_URL

def criar_perfil(perfil_data):
    try:
        response = requests.post(f"{API_URL}/api/v1/user/create", json=perfil_data)
        return response.json()
    except Exception as e:
        return {"status": "erro", "detalhe": str(e)}
