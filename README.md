# ETL_API_BTC

## 📝 Descrição
Projeto de ETL (Extract, Transform, Load) para dados relacionados ao Bitcoin (BTC). Este projeto coleta, processa e armazena dados sobre o Bitcoin para análise e visualização, implementando diferentes abordagens de armazenamento e processamento.

## 🔄 Pipelines

### pipeline_00.py
- Implementação básica de ETL
- Extração e tratamento dos dados
- Sem persistência de dados

### pipeline_01.py
- Extração e tratamento dos dados
- Armazenamento local em JSON utilizando TinyDB
- Permite consultas simples aos dados armazenados

### pipeline_02.py
- Implementação com SQLAlchemy
- Armazenamento em banco de dados SQL
- Modelagem de dados usando ORM
- Permite consultas complexas e relacionamentos

### pipeline_03.py
- Versão mais avançada com recursos adicionais
- Implementação de logging
- Tratamento de erros aprimorado
- Configurações via arquivo .env

## 🚀 Funcionalidades
- Extração de dados de preços do Bitcoin de diversas fontes
- Transformação e limpeza dos dados coletados
- Múltiplas opções de armazenamento (JSON, SQL)
- Análise histórica de preços
- Visualizaç��o de dados através de gráficos
- Logging e monitoramento
- Configuração flexível via variáveis de ambiente

## 🛠️ Tecnologias Utilizadas
- Python
- Pandas (manipulação de dados)
- Requests (requisições HTTP)
- TinyDB (armazenamento JSON)
- SQLAlchemy (ORM e banco de dados SQL)
- python-dotenv (configurações)
- logging (registros de execução)

## ⚙️ Instalação
1. Clone o repositório:

git clone https://github.com/seu-usuario/ETL_BTC.git

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
- Crie um arquivo `.env` baseado no exemplo `.env.example`
- Ajuste as configurações conforme necessário

## 🚦 Como Usar
1. Escolha a pipeline adequada para seu caso de uso:
   - `pipeline_00.py` para testes rápidos sem persistência
   - `pipeline_01.py` para armazenamento simples em JSON
   - `pipeline_02.py` para uso com banco de dados SQL
   - `pipeline_03.py` para ambiente de produção com logging

2. Execute a pipeline escolhida:
```bash
python pipeline_XX.py
```

