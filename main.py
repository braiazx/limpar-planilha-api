from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
import uvicorn
import os

app = FastAPI()

class PlanilhaEntrada(BaseModel):
    rows: List[Dict[str, str]]

@app.post("/limpar-planilha")
async def limpar_planilha(data: PlanilhaEntrada):
    dados_limpos = []
    for row in data.rows:
        nova_linha = {k: v.strip().upper() for k, v in row.items() if v and v.strip() != ""}
        if nova_linha:
            dados_limpos.append(nova_linha)
    return {"rows_limpos": dados_limpos}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
