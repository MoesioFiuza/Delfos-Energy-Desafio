from fastapi import FastAPI
from rotas import rota

app = FastAPI()

app.include_router(rota)

@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}
