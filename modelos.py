from sqlalchemy import Column, Float, TIMESTAMP
from banco_dados import Base

class Dados(Base):
    __tablename__ = "dados"

    timestamp = Column(TIMESTAMP, primary_key=True)
    velocidade_vento = Column(Float, nullable=False)
    potencia = Column(Float, nullable=False)
    temperatura_ambiente = Column(Float, nullable=False)
