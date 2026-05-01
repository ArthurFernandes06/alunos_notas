from pydantic import BaseModel

class ProvasSchema(BaseModel):
    id: int | None = None
    nome: str