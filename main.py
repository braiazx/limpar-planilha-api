from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from collections import Counter

app = FastAPI()

class LinhaPlanilha(BaseModel):
    rows: List[Dict[str, str]]

@app.post("/filtrar-assuntos")
async def filtrar_assuntos(data: LinhaPlanilha):
    linhas = data.rows

    # Conta a ocorrência de cada valor na coluna "assunto"
    contagem = Counter([linha.get("assunto", "").strip() for linha in linhas])

    # Filtra os que aparecem 3 vezes ou mais
    linhas_filtradas = [
        linha for linha in linhas
        if contagem.get(linha.get("assunto", "").strip(), 0) >= 3
    ]

    return {"linhas_validas": linhas_filtradas}
