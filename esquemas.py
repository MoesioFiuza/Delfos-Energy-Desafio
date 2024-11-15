from pydantic import BaseModel
from datetime import datetime

class DadosSchema(BaseModel):
    timestamp: datetime
    velocidade_vento: float
    potencia: float
    temperatura_ambiente: float

    class Config:
        orm_mode = True

class DadosCriacao(BaseModel):
    velocidade_vento: float
    potencia: float
    temperatura_ambiente: float
