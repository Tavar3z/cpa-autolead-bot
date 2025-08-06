import pandas as pd

try:
    # Lê a aba "api" da planilha
    df = pd.read_excel(r"caminho da planilha", sheet_name="api", header=None)
    API_URL = str(df.iloc[1, 0]).strip()  # Pega o valor da célula A2
except Exception as e:
    raise Exception(f"Erro ao carregar API URL da aba 'api': {e}")

# Constantes para o payload
IOS = "iOS"

# ATENÇÃO: group_id precisa ser int, não string
GROUP_ID = 6945137   # coloque aqui o ID real assim que souber
