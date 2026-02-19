import requests
import pandas as pd
from datetime import datetime, timedelta

moedas = {
    "USD": 10813,
    "EUR": 21619,
    "GBP": 21623,
    "JPY": 21621,
    "ARS": 3549,
    "CHF": 21625
}

dias = 30

hoje = datetime.today()
data_final = hoje.strftime("%d/%m/%Y")
data_inicial = (hoje - timedelta(days=dias)).strftime("%d/%m/%Y")

lista = []

for moeda in moedas:
    codigo = moedas[moeda]

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"

    parametros = {
        "formato": "json",
        "dataInicial": data_inicial,
        "dataFinal": data_final
    }

    resposta = requests.get(url, params=parametros)
    dados = resposta.json()

    for item in dados:
        lista.append({
            "Data": item["data"],
            "Moeda": moeda,
            "Valor": float(item["valor"])
        })

df = pd.DataFrame(lista)

df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

df.to_excel("cotacoes_moedas.xlsx", index=False)

print("Arquivo cotacoes_moedas.xlsx foi criado")
