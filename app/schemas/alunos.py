from pydantic import BaseModel

class AlunosSchema(BaseModel):
    id: int | None = None
    nome: str
    matricula: str
    turma: str