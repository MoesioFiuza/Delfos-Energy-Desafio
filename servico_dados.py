from sqlalchemy.orm import Session
from modelos import Dados
from datetime import datetime

def obter_dados(sessao: Session, inicio: datetime, fim: datetime):
    return sessao.query(Dados).filter(Dados.timestamp >= inicio, Dados.timestamp <= fim).all()

def obter_dados_por_variavel(sessao: Session, inicio: datetime, fim: datetime, variavel: str):
    consulta = sessao.query(Dados.timestamp)
    if variavel == "velocidade_vento":
        consulta = consulta.add_columns(Dados.velocidade_vento)
    elif variavel == "potencia":
        consulta = consulta.add_columns(Dados.potencia)
    elif variavel == "temperatura_ambiente":
        consulta = consulta.add_columns(Dados.temperatura_ambiente)
    consulta = consulta.filter(Dados.timestamp >= inicio, Dados.timestamp <= fim)
    return consulta.all()

def inserir_dados(sessao: Session, novo_dado: Dados):
    sessao.add(novo_dado)
    sessao.commit()
    sessao.refresh(novo_dado)
    return novo_dado
