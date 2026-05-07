from pydantic import BaseModel

class ProvasSchema(BaseModel):
    id: int | None = None
    nome: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "nome": "Matemática"
            }
        }
    }

