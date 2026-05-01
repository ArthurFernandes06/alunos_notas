from app.schemas import AlunosSchema

async def listar_todos_alunos() -> list[AlunosSchema]:
    pass

async def buscar_aluno(id: int) -> AlunosSchema:
    pass

async def cadastrar_aluno(aluno: AlunosSchema) -> bool:
    pass

async def atualizar_aluno(aluno: AlunosSchema) -> bool:
    pass

async def deletar_aluno(aluno: AlunosSchema) -> bool:
    pass
