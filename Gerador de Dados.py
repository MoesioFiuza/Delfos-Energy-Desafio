import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from banco_dados import SessaoFonte
from modelos import Dados  

def gerar_dados_aleatorios(sessao: Session, dias: int = 10):
    data_final = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    data_inicial = data_final - timedelta(days=dias)
    data_atual = data_inicial

    # Inserir dados com intervalo de 1 minuto
    registros = []
    while data_atual < data_final:
        velocidade_vento = round(random.uniform(0, 25), 2)  
        potencia = round(random.uniform(0, 100), 2)         
        temperatura_ambiente = round(random.uniform(-10, 40), 2)  

        dado = Dados(
            timestamp=data_atual,
            velocidade_vento=velocidade_vento,
            potencia=potencia,
            temperatura_ambiente=temperatura_ambiente
        )

        registros.append(dado)
        data_atual += timedelta(minutes=1)

    
    sessao.bulk_save_objects(registros)
    sessao.commit()
    print(f"{len(registros)} registros inseridos com sucesso no intervalo de {dias} dias.")

if __name__ == "__main__":
    with SessaoFonte() as sessao:
        gerar_dados_aleatorios(sessao)
