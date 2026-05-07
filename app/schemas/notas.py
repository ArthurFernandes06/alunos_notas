from pydantic import BaseModel

class NotasSchema(BaseModel):
    id: int | None = None
    id_prova: int 
    id_aluno: int
    nota: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "id_aluno": 1,
                "id_prova": 2,
                "nota": 6.7
            }
        }
    }

