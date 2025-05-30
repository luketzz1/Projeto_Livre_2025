import json
from models.turma import Turma

def salvar_turma_em_json(turma: Turma, caminho: str):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(turma.to_dict(), f, indent=4)

def carregar_turma_de_json(caminho: str) -> Turma:
    with open(caminho, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Turma.from_dict(data)