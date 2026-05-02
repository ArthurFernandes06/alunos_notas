from schemas import ProvasSchema
from core import ConnectionDB

def listar_todas_provas() -> list[ProvasSchema]:
    
    pass

def buscar_prova(id: int) -> ProvasSchema:
    pass

def cadastrar_prova(prova: ProvasSchema) -> bool:
    queryStr = """
        INSERT INTO provas (nome) VALUES (%s);
    """
    sucess_operation = True
    with ConnectionDB() as cursor:
        values = (prova.nome,)

        try:
            cursor.execute(queryStr, values)

        except Exception as ex:
            print(ex)
            sucess_operation = False

    return sucess_operation 


def atualizar_prova(prova: ProvasSchema) -> bool:
    pass

def deletar_prova(id: int) -> bool:
    pass