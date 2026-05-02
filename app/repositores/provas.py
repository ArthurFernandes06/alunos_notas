from schemas import ProvasSchema
from core import ConnectionDB

def listar_todas_provas() -> list[ProvasSchema]:
    #Retorna uma lista com objetos ProvasSchemas
    todas_provas = list()
    queryStr = """ 
        SELECT id, nome FROM provas;
    """
    with ConnectionDB() as cursor:
        try:
            cursor.execute(queryStr)
            results = cursor.fetchall()

            for result in results:
                prova = ProvasSchema(id=result[0], nome=result[1])
                todas_provas.append(prova)
        except Exception as ex:
            print(ex)
        
    return todas_provas


def buscar_prova(id: int) -> ProvasSchema:
    #Se a buscar dor bem sucedida retorna um ProvaSchema,
    #caso contrário retorna None
    queryStr = """
        SELECT id, nome FROM provas WHERE id = %s
    """
    prova = None
    with ConnectionDB() as cursor:
        try:
            cursor.execute(queryStr,(id,))
            result = cursor.fetchone()
            if result:
                prova = ProvasSchema(id=result[0], nome=result[1])

        except Exception as ex:
            print(ex)
    
    return prova

def cadastrar_prova(prova: ProvasSchema) -> bool:
    queryStr = """
        INSERT INTO provas (nome) VALUES (%s);
    """
    sucess_operation = False
    with ConnectionDB() as cursor:
        values = (prova.nome,)
        try:
            cursor.execute(queryStr, values)
            sucess_operation = True

        except Exception as ex:
            print(ex)
            
    return sucess_operation 


def atualizar_prova(prova: ProvasSchema) -> bool:
    queryStr = """
        UPDATE provas  
        SET nome = %s 
        WHERE id = %s;
    """
    sucess_operation = False
    values = (prova.nome, prova.id,)

    #Valida se os atributos id é != None
    if prova.id:
        with ConnectionDB() as cursor:
            try:
                cursor.execute(queryStr, values)
                sucess_operation = True
            except Exception as ex:
                print(ex)

    return sucess_operation

def deletar_prova(id: int) -> bool:
    queryStr = """
        DELETE FROM provas WHERE id = %s;
    """
    sucess_operation = False
    with ConnectionDB() as cursor:
        try:
            cursor.execute(queryStr, (id,))
            sucess_operation = True
        except Exception as ex:
            print(ex)

    return sucess_operation
