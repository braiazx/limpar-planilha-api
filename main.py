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

    # ✅ Campo correto da planilha: "Assunto (J)"
    # Conta quantas vezes cada assunto aparece
    contagem = Counter([linha.get("Assunto (J)", "").strip() for linha in linhas])

    # Filtra apenas linhas cujo "Assunto (J)" aparece 3 vezes ou mais
    linhas_filtradas = [
        linha for linha in linhas
        if contagem.get(linha.get("Assunto (J)", "").strip(), 0) >= 3
    ]

    return {"linhas_validas": linhas_filtradas}

