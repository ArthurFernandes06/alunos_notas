from app.schemas import NotasSchema

async def listar_todas_notas() -> list[NotasSchema]:
    pass

async def buscar_nota(id: int) -> NotasSchema:
    pass

async def cadastrar_nota(nota: NotasSchema) -> bool:
    pass

async def atualizar_nota(nota: NotasSchema) -> bool:
    pass

async def deletar_nota(nota: NotasSchema) -> bool:
    pass
