from pydantic import BaseModel

class NotasSchema(BaseModel):
    id: int | None = None
    id_prova: int 
    id_aluno: int
    nota: float