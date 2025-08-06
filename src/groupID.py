import requests
from config import API_URL

def listar_grupos():
    url = f"{API_URL}/api/v1/group/list"
    resp = requests.get(url)
    print("Status:", resp.status_code)
    print("Resposta bruta:", resp.text)

    data = resp.json()
    if data.get("code") == 0:
        for g in data["data"]["list"]:
            print(f"ID real: {g['group_id']}  → Nome: {g['group_name']}")
    else:
        print(f"Erro da API: {data.get('msg')}")

if __name__ == "__main__":
    listar_grupos()
