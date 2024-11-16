import httpx
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

DB_ALVO_URL = "postgresql://alvo_user:alvo_pass@db_alvo:5432/alvo_db"
API_URL = "http://fastapi_etl:8000/dados"

def etl_processo(data: str):
    try:
        
        data_inicial = datetime.strptime(data, "%Y-%m-%d")
        data_final = data_inicial + timedelta(days=1)

        params = {
            "inicio": data_inicial.isoformat(),
            "fim": data_final.isoformat(),
            "variaveis": "velocidade_vento,potencia"
        }
        print(f"Consultando API com parâmetros: {params}")

        
        response = httpx.get(API_URL, params=params, follow_redirects=False)

        
        print(f"URL requisitada: {response.url}")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Resposta Bruta: {response.text}")

        if response.status_code == 307:
            print(f"Redirecionado para: {response.headers.get('location')}")
            raise Exception(f"Redirecionamento inesperado para: {response.headers.get('location')}")

        if response.status_code != 200:
            raise Exception(f"Erro ao consultar a API: {response.text}")

        
        dados = response.json()

        if not dados:
            raise Exception("Nenhum dado retornado pela API.")

        print(f"Número de registros retornados: {len(dados)}")

        
        df = pd.DataFrame(dados)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        agregados = df.resample("10T", on="timestamp").agg({
            "velocidade_vento": ["mean", "min", "max", "std"],
            "potencia": ["mean", "min", "max", "std"]
        })
        agregados.columns = ['_'.join(col) for col in agregados.columns]
        agregados.reset_index(inplace=True)

        
        engine = create_engine(DB_ALVO_URL)
        with engine.connect() as conn:
            agregados.to_sql("dados_agregados", con=conn, if_exists="append", index=False)
        print("Processo ETL concluído com sucesso.")

    except Exception as e:
        print(f"Erro no processo ETL: {e}")

if __name__ == "__main__":
    data_input = input("Digite a data (YYYY-MM-DD): ")
    etl_processo(data_input)
