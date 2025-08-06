import os
import pandas as pd
import json
import time
import random
import sys
from src.utils import parse_proxy
from src.ads_power_api import criar_perfil
from src.config import API_URL, GROUP_ID

# Lista de versões iOS suportadas
ios_versions = ["iOS 12", "iOS 13", "iOS 14", "iOS 15", "iOS 16", "iOS 17", "iOS 18"]

if getattr(sys, 'frozen', False):
    caminho_base = os.path.dirname(sys.executable)
else:
    caminho_base = os.path.dirname(os.path.abspath(__file__))

caminho_excel = os.path.join(caminho_base, "data", "perfis.xlsx")

# Verifica se o arquivo existe antes de tentar ler
if not os.path.exists(caminho_excel):
    raise FileNotFoundError(f"Arquivo não encontrado: {caminho_excel}")

# Lê a aba 'dados' da planilha
df = pd.read_excel(caminho_excel, sheet_name="dados")

for _, row in df.iterrows():
    try:
        proxy_info = parse_proxy(str(row["proxy"]).strip())

        # Sorteia uma versão de iOS aleatória
        ios_escolhido = random.choice(ios_versions)
        versao_numerica = ios_escolhido.replace("iOS ", "").replace(".", "_")

        user_agent_ios = (
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {versao_numerica} like Mac OS X) "
            f"AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{versao_numerica.split('_')[0]}.0 "
            "Mobile/15E148 Safari/604.1"
        )

        payload = {
            "group_id": int(GROUP_ID),
            "name": str(row["nome"]),
            "open_urls": [str(row.get("start_url", "")).strip()],
            "proxy_type": 1,
            "user_proxy_config": {
                "proxy_soft": "other",
                "proxy_type": "http",
                "proxy_host": str(proxy_info["proxy_host"]),
                "proxy_port": str(proxy_info["proxy_port"]),
                "proxy_user": str(proxy_info["proxy_user"]),
                "proxy_password": str(proxy_info["proxy_password"])
            },
            "fingerprint_config": {
                "language": ["en-US"],
                "ua": user_agent_ios,
                "flash": "block",
                "scan_port_type": "1",
                "screen_resolution": "375_812",
                "fonts": ["all"],
                "longitude": "180",
                "latitude": "90",
                "webrtc": "proxy",
                "do_not_track": "true",
                "hardware_concurrency": "default",
                "device_memory": "default"
            }
        }

        print(f"[DEBUG PAYLOAD ENVIADO] →\n{json.dumps(payload, indent=2)}")
        resultado = criar_perfil(payload)
        print(f"[{row['nome']}] → {resultado}")

        time.sleep(1.5)

    except Exception as e:
        print(f"[ERRO] {row.get('nome', 'NOME DESCONHECIDO')}: {e}")
