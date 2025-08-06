from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class LinhaPlanilha(BaseModel):
    rows: List[Dict[str, str]]

@app.post("/padronizar-maiusculo")
async def padronizar_maiusculo(data: LinhaPlanilha):
    linhas = data.rows

    # Para cada linha, transforma todos os valores em maiúsculo
    linhas_formatadas = []
    for linha in linhas:
        nova_linha = {chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in linha.items()}
        linhas_formatadas.append(nova_linha)

    return {"linhas_maiusculas": linhas_formatadas}

