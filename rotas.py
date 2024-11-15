from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from banco_dados import obter_sessao
from esquemas import DadosSchema, DadosCriacao
from servico_dados import obter_dados, obter_dados_por_variavel, inserir_dados
from modelos import Dados
from datetime import datetime
from typing import List, Optional

rota = APIRouter()

@rota.get("/dados", response_model=List[DadosSchema])
def listar_dados(
    inicio: datetime,
    fim: datetime,
    variavel: Optional[str] = None,
    sessao: Session = Depends(obter_sessao)
):
    if variavel:
        dados = obter_dados_por_variavel(sessao, inicio, fim, variavel)
    else:
        dados = obter_dados(sessao, inicio, fim)
    if not dados:
        raise HTTPException(status_code=404, detail="Dados não encontrados para o intervalo especificado.")
    return dados

@rota.post("/dados", response_model=DadosSchema)
def criar_dado(dado: DadosCriacao, sessao: Session = Depends(obter_sessao)):
    novo_dado = Dados(
        timestamp=datetime.utcnow(),
        velocidade_vento=dado.velocidade_vento,
        potencia=dado.potencia,
        temperatura_ambiente=dado.temperatura_ambiente
    )
    return inserir_dados(sessao, novo_dado)
