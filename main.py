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
    contagem = Counter([linha.get("Assunto (J)", "").strip() for linha in linhas])
    linhas_filtradas = [
        linha for linha in linhas
        if contagem.get(linha.get("Assunto (J)", "").strip(), 0) >= 3
    ]
    return {"linhas_validas": linhas_filtradas}

