from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from banco_dados import obter_sessao
from esquemas import DadosSchema
from servico_dados import obter_dados
from datetime import datetime
from typing import List

rota = APIRouter()

@rota.get("/dados", response_model=List[DadosSchema])
def listar_dados(
    inicio: datetime,
    fim: datetime,
    sessao: Session = Depends(obter_sessao)
):
    try:
        dados = obter_dados(sessao, inicio, fim)
        if not dados:
            raise HTTPException(status_code=404, detail="Dados não encontrados.")
        return dados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
