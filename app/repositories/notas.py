from app.schemas import NotasSchema

def listar_todas_notas() -> list[NotasSchema]:
    pass

def buscar_nota(id: int) -> NotasSchema:
    pass

def buscar_notas_aluno(id: int, id_aluno: int) ->list[NotasSchema]:
    pass

def buscar_notas_prova(id: int, id_prova: int) -> list[NotasSchema]:
    pass

def cadastrar_nota(nota: NotasSchema) -> bool:
    pass

def atualizar_nota(nota: NotasSchema) -> bool:
    pass

def deletar_nota(nota: NotasSchema) -> bool:
    pass
