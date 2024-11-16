import httpx
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

# Configurações de conexão
DB_ALVO_URL = "postgresql://alvo_user:alvo_pass@db_alvo:5432/alvo_db"
API_URL = "http://fastapi_etl:8000/dados/"

def etl_processo(data: str):
    # Converter a data para datetime e calcular intervalo de 1 dia
    data_inicial = datetime.strptime(data, "%Y-%m-%d")
    data_final = data_inicial + timedelta(days=1)

    # Consultar a API para os dados do intervalo
    params = {
        "inicio": data_inicial.isoformat(),
        "fim": data_final.isoformat(),
        "variaveis": ["velocidade_vento", "potencia"]
    }
    response = httpx.get(API_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Erro ao consultar a API: {response.text}")

    dados = response.json()

    # Transformar os dados com Pandas
    df = pd.DataFrame(dados)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    agregados = df.resample("10T", on="timestamp").agg({
        "velocidade_vento": ["mean", "min", "max", "std"],
        "potencia": ["mean", "min", "max", "std"]
    })
    agregados.columns = ['_'.join(col) for col in agregados.columns]
    agregados.reset_index(inplace=True)

    # Conectar ao banco `db_alvo` e salvar os dados
    engine = create_engine(DB_ALVO_URL)
    Session = sessionmaker(bind=engine)

    with Session() as sessao:
        agregados.to_sql("dados_agregados", con=engine, if_exists="append", index=False)

    print("Processo ETL concluído com sucesso.")

# Executar o ETL
if __name__ == "__main__":
    data_input = input("Digite a data (YYYY-MM-DD): ")
    etl_processo(data_input)
