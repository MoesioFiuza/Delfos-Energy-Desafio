from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL do banco de dados Fonte, obtida das variáveis de ambiente
URL_BANCO_DADOS = os.getenv("DATABASE_FONTE_URL")

# Configurações do SQLAlchemy
motor = create_engine(URL_BANCO_DADOS)
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)
Base = declarative_base()

# Dependência para obter uma sessão de banco de dados
def obter_sessao():
    sessao = SessaoLocal()
    try:
        yield sessao
    finally:
        sessao.close()
