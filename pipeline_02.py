import requests
from datetime import datetime
import time
from sqlalchemy import create_engine # para criar o engine ( a tabela do banco de dados)
from sqlalchemy.orm import sessionmaker # para criar a sessão
from database import Base, BitcoinPreco # Importar Base e BitcoinPreco do database.py
import os
from dotenv import load_dotenv


# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão ao banco PostgreSQL (sem ?sslmode=...)
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada/verificada com sucesso!")

# Extrai os dados do BTC diretamente da API da Coinbase
def extract_dados_btc():
    url = "https://api.coinbase.com/v2/prices/spot"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro na API: {response.status_code}')

    
    return None


# Trata os dados brutos da API em um formato mais legível e adiciona timestamp
def transform_dados_btc(dados):
    valor = float(dados['data']['amount'])
    cripto = dados['data']['base']
    moeda = dados['data']['currency']
    timestamp = datetime.now()
   
# Cria um dicionário com os dados do BTC

    dados_transformados = {
        'valor': valor,
        'cripto': cripto,
        'moeda': moeda,
        'timestamp': timestamp
    }
    return dados_transformados

def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")


if __name__ == "__main__":

    criar_tabela()
    print("Iniciando ELT com atualização automática a cada 15s - ctrl+c para interromper")
    while True:
        try:
            dados = extract_dados_btc()
            if dados:
                dados_tratados = transform_dados_btc(dados)
                print("Dados tratados:", dados_tratados)
                salvar_dados_postgres(dados_tratados) 

            time.sleep(15)
        except KeyboardInterrupt:
            print("\nPRocesso interrompido pelo usuário. Finalizando")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)