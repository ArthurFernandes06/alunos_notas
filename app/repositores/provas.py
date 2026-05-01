from app.schemas import ProvasSchema

async def listar_todas_provas() -> list[ProvasSchema]:
    pass

async def buscar_prova(id: int) -> ProvasSchema:
    pass

async def cadastrar_prova(prova: ProvasSchema) -> bool:
    pass

async def atualizar_prova(prova: ProvasSchema) -> bool:
    pass

async def deletar_prova(id: int) -> bool:
    pass