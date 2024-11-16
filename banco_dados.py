import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from fastapi import Depends

load_dotenv()

URL_BANCO_FONTE = (
    f"postgresql://{os.getenv('FONTE_DB_USER')}:{os.getenv('FONTE_DB_PASSWORD')}"
    f"@{os.getenv('FONTE_DB_HOST')}:{os.getenv('FONTE_DB_PORT')}/{os.getenv('FONTE_DB_NAME')}"
)

URL_BANCO_ALVO = (
    f"postgresql://{os.getenv('ALVO_DB_USER')}:{os.getenv('ALVO_DB_PASSWORD')}"
    f"@{os.getenv('ALVO_DB_HOST')}:{os.getenv('ALVO_DB_PORT')}/{os.getenv('ALVO_DB_NAME')}"
)

if not URL_BANCO_FONTE or not URL_BANCO_ALVO:
    raise ValueError("As URLs dos bancos de dados não foram geradas corretamente.")

motor_fonte = create_engine(URL_BANCO_FONTE)
SessaoFonte = sessionmaker(autocommit=False, autoflush=False, bind=motor_fonte)

motor_alvo = create_engine(URL_BANCO_ALVO)
SessaoAlvo = sessionmaker(autocommit=False, autoflush=False, bind=motor_alvo)

Base = declarative_base()

def obter_sessao():
    sessao = SessaoFonte()
    try:
        yield sessao
    finally:
        sessao.close()
