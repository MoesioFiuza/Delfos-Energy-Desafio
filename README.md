
# Delfos Energy - Desafio


Essa é a solução que eu implementaria para um ETL





## Visão geral do Projeto
├── .env                # Configurações de ambiente docker

├── docker-compose.yml  # Configuração dos containers Docker

├── Dockerfile          # Imagem base para FastAPI e ETL

├── banco_dados.py      # Conexão com os bancos de dados

├── esquemas.py         # Definição dos modelos Pydantic

├── etl_script.py       # Script ETL

├── Gerador de Dados.py # Script para popular o banco fonte

├── main.py             # Arquivo principal da API

├── modelos.py          # Modelos SQLAlchemy

├── requirements.txt    # Dependências do projeto

├── rotas.py            # Rotas da API

└── servico_dados.py    # Lógica de acesso ao banco de dados





## Requisitos

Python 3.10+

(-)Docker  

(-)Docker-Compose

(-)Git
## Configuração do Ambiente

Abra o terminal ou CMD

Clone este repositório:
git clone https://github.com/MoesioFiuza/Delfos-Energy-Desafio.git

Mude de pasta para o repositório com:
"cd Delfos-Energy-Desafio"


Recomendação é por criar um ambiente virtual para prevenir possíveis conflitos entre bibliotecas previamente instaladas na sua máquina:

python3 -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows

Instale as dependências com:

pip install -r requirements.txt





## Uso


1. Executar o Projeto com Docker

Iniciar os containers:


docker-compose up --build


FastAPI estará disponível em: http://localhost:8000


2. Gerar Dados no Banco de Dados Fonte

Execute o script Gerador de Dados.py dentro do container fastapi_etl:


docker exec -it fastapi_etl python Gerador\ de\ Dados.py


Apos a execução do script Gerador de Dados.py você verá a mensagem no terminal:

"14400 registros inseridos com sucesso no intervalo de 10 dias."

Você pode verificar diretamente no banco de dados Fonte através do comando:

"docker exec -it db_fonte psql -U fonte_user -d fonte_db"

Que acessará o banco de dados Fonte, no qual você pode executar a seguinte query:


"SELECT * FROM dados LIMIT 10;"

O output será esse:





      timestamp      | velocidade_vento | potencia | temperatura_ambiente 

        Você verá uma série de dados que vai depender do dia e hora de
        execução do script Gerador de Dados.py 
 
 (10 rows)



Digite o comando "\q" para sair do banco de dados Fonte


Nota: É importante salientar que o script Gerador de Dados se valerá do dia de sua execução e contará 10 dias corridos no passado. Sendo esse o Range temporal que estará salvo no Banco de Dados Fonte



3. Executar o ETL



Para rodar o script ETL e transferir os dados para o banco de dados alvo:

"docker exec -it fastapi_etl python /app/etl_script.py"

Digite a data no formato YYYY-MM-DD para selecionar os dados do dia, lembrando que o range temporal está vinculado ao dia da execução do script Gerador de Dados.py


Você verá todos os dados que a API moveu de um banco para o outro, seguido da mensagem "Processo ETL concluído com sucesso."












## Considerações finais


Quero agradecer pela oportunidade de mostrar um pouco do como eu trabalho, bem como meu racíocinio em construção de algoritmos. Desejo um bom dia, boa tarde ou boa noite à todas as pessoas da Delfos Energy. Muito Obrigado!
