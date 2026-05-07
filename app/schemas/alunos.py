from pydantic import BaseModel

class AlunosSchema(BaseModel):
    id: int | None = None
    matricula: str
    nome: str
    turma: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "matricula": "2025001",
                "nome": "Cleiton",
                "turma": "3A"
            }
        }
    }