import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from fastapi import Depends

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# URL do banco de dados Fonte
URL_BANCO_FONTE = (
    f"postgresql://{os.getenv('FONTE_DB_USER')}:{os.getenv('FONTE_DB_PASSWORD')}"
    f"@{os.getenv('FONTE_DB_HOST')}:{os.getenv('FONTE_DB_PORT')}/{os.getenv('FONTE_DB_NAME')}"
)

# URL do banco de dados Alvo
URL_BANCO_ALVO = (
    f"postgresql://{os.getenv('ALVO_DB_USER')}:{os.getenv('ALVO_DB_PASSWORD')}"
    f"@{os.getenv('ALVO_DB_HOST')}:{os.getenv('ALVO_DB_PORT')}/{os.getenv('ALVO_DB_NAME')}"
)

# Verificação das URLs dos bancos de dados
if not URL_BANCO_FONTE or not URL_BANCO_ALVO:
    raise ValueError("As URLs dos bancos de dados não foram geradas corretamente.")

# Configuração do SQLAlchemy para o banco de dados Fonte
motor_fonte = create_engine(URL_BANCO_FONTE)
SessaoFonte = sessionmaker(autocommit=False, autoflush=False, bind=motor_fonte)

# Configuração do SQLAlchemy para o banco de dados Alvo
motor_alvo = create_engine(URL_BANCO_ALVO)
SessaoAlvo = sessionmaker(autocommit=False, autoflush=False, bind=motor_alvo)

# Base para os modelos SQLAlchemy
Base = declarative_base()

# Função para obter uma sessão do banco de dados Fonte
def obter_sessao():
    sessao = SessaoFonte()
    try:
        yield sessao
    finally:
        sessao.close()
