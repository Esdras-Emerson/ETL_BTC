import requests
from tinydb import TinyDB, Query
from datetime import datetime

# Extrai os dados do BTC diretamente da API da Coinbase
def extract_dados_btc():
    url = "https://api.coinbase.com/v2/prices/spot"

    response = requests.get(url)

    dados = (response.json())
    return dados


# Transforma os dados do BTC em um formato mais legível
def trasform_dados_btc(dados):
    valor = dados['data']['amount']
    cripto = dados['data']['base']
    moeda = dados['data']['currency']
    timestamp = datetime.now().timestamp()
   

    dados_tranformados = {
        'valor': valor,
        'cripto': cripto,
        'moeda': moeda,
        'timestamp': timestamp
    }
    return dados_tranformados

# Salva os dados do BTC em um banco de dados TinyDB (noSQL)
def salvar_dados_tinydb(dados, db_name="btc.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso!")


if __name__ == "__main__":
    dados = extract_dados_btc()
    dados_tratados = trasform_dados_btc(dados)
    salvar_dados_tinydb(dados_tratados)