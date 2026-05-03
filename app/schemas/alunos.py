from pydantic import BaseModel

class AlunosSchema(BaseModel):
    id: int | None = None
    matricula: str
    nome: str
    matricula: str
    turma: str