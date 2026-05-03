from app.schemas import ProvasSchema
from app.core import ConnectionDB

def listar_todas_provas() -> list[ProvasSchema]:
    #Retorna uma lista com objetos ProvasSchemas
    todas_provas = list()
    queryStr = """ 
        SELECT id, nome FROM provas;
    """
    with ConnectionDB() as cursor:
        cursor.execute(queryStr)
        results = cursor.fetchall()

        for result in results:
            prova = ProvasSchema(id=result[0], nome=result[1])
            todas_provas.append(prova)

        
    return todas_provas


def buscar_prova(id: int) -> ProvasSchema | None:
    #Se a buscar dor bem sucedida retorna um ProvaSchema,
    #caso contrário retorna None
    queryStr = """
        SELECT id, nome FROM provas WHERE id = %s
    """
    prova = None
    with ConnectionDB() as cursor:   
        cursor.execute(queryStr,(id,))
        result = cursor.fetchone()
        if result:
            prova = ProvasSchema(id=result[0], nome=result[1])

    return prova

def cadastrar_prova(prova: ProvasSchema) -> ProvasSchema:
    queryStr = """
        INSERT INTO provas (nome) VALUES (%s);
    """
    
    with ConnectionDB() as cursor:
        values = (prova.nome,)
        cursor.execute(queryStr, values)
        prova.id = cursor.lastrowid

    return prova



def atualizar_prova(prova: ProvasSchema) -> None:
    queryStr = """
        UPDATE provas  
        SET nome = %s 
        WHERE id = %s;
    """
    values = (prova.nome, prova.id,)
    #Valida se os atributos id é != None
    if prova.id != None:
        with ConnectionDB() as cursor:      
            cursor.execute(queryStr, values)
            if cursor.rowcount == 0:
                raise ValueError("Prova não encontrada.")
    else:
        raise ValueError("Requisição sem id.")

        

def deletar_prova(id: int) -> None:
    queryStr = """
        DELETE FROM provas WHERE id = %s;
    """

    with ConnectionDB() as cursor:  
        cursor.execute(queryStr, (id,))
        if cursor.rowcount == 0:
            raise ValueError("Prova não encontrada.")
