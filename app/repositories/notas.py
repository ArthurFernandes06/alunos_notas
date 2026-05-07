from app.schemas import NotasSchema
from app.core import ConnectionDB
def listar_todas_notas() -> list[NotasSchema]:
    queryStr = """
        SELECT id, id_aluno, id_prova, nota FROM notas;
    """
    lista_notas = list()
    with ConnectionDB() as cursor:
        cursor.execute(queryStr)
        results = cursor.fetchall()
        for result in results:
            nota = NotasSchema(
                id= result[0],
                id_aluno=result[1],
                id_prova= result[2],
                nota=result[3]
            )
            lista_notas.append(nota)
    
    return lista_notas


def buscar_nota(id_nota: int) -> NotasSchema | None:
    queryStr = """
        SELECT id, id_aluno, id_prova, nota FROM notas 
        WHERE id = %s;
    """
    nota = None
    with ConnectionDB() as cursor:
        cursor.execute(queryStr, (id_nota, ))
        result = cursor.fetchone()
        if result:
            nota = NotasSchema(
                id= result[0],
                id_aluno= result[1],
                id_prova= result[2],
                nota= result[3]
            )
    return nota


def buscar_notas_aluno(id_aluno: int) ->list[NotasSchema]:
    queryStr = """
        SELECT id, id_aluno, id_prova, nota FROM notas 
        WHERE id_aluno = %s;
    """
    lista_notas = list()
    with ConnectionDB() as cursor:
        cursor.execute(queryStr, (id_aluno, ))
        results = cursor.fetchall()
        for result in results:
            nota = NotasSchema(
                id= result[0],
                id_aluno= result[1],
                id_prova= result[2],
                nota= result[3]
            )
            lista_notas.append(nota)
    return lista_notas

def buscar_notas_prova(id_prova: int) -> list[NotasSchema]:
    queryStr = """
        SELECT id, id_aluno, id_prova, nota FROM notas 
        WHERE id_prova = %s;
    """
    lista_notas = list()
    with ConnectionDB() as cursor:
        cursor.execute(queryStr, (id_prova, ))
        results = cursor.fetchall()
        for result in results:
            nota = NotasSchema(
                id= result[0],
                id_aluno= result[1],
                id_prova= result[2],
                nota= result[3]
            )
            lista_notas.append(nota)
    return lista_notas

def buscar_nota_prova_aluno(id_aluno: int, id_prova: int) -> NotasSchema | None:
    queryStr = """
        SELECT id, id_aluno, id_prova, nota FROM notas 
        WHERE id_aluno = %s AND id_prova = %s;
    """
    nota = None
    values = (id_aluno, id_prova, ) 
    with ConnectionDB() as cursor:
        cursor.execute(queryStr, values)
        result = cursor.fetchone()
        if result:
            nota = NotasSchema(
                id= result[0],
                id_aluno= result[1],
                id_prova= result[2],
                nota= result[3]
            )

    return nota

def cadastrar_nota(nota: NotasSchema) -> NotasSchema:
    queryStr = """
        INSERT INTO notas (id_aluno, id_prova, nota) 
        VALUES (%s, %s, %s);
    """
    values = (nota.id_aluno, nota.id_prova, nota.nota,)
    try:
        with ConnectionDB() as cursor:
            cursor.execute(queryStr, values)
            nota.id = cursor.lastrowid
    except Exception as ex:
        if hasattr(ex, "args"):
            if ex.args[0] == 1062:
                raise ValueError("Essa nota já está cadastrada")
            elif ex.args[0] == 1452:
                raise ValueError("Aluno ou prova não existe")
            
        raise
        
    return nota

def atualizar_nota(nota: NotasSchema) -> None:
    queryStr = """
        UPDATE notas 
        SET id_aluno = %s, id_prova = %s, nota = %s
        where id = %s;
    """
    if nota.id is None:
        raise ValueError("Requisição sem id")
    
    values = (nota.id_aluno, nota.id_prova, nota.nota, nota.id, )
    try:
        with ConnectionDB() as cursor:
            #Verifica se o registro já existe
            cursor.execute("SELECT * FROM notas WHERE id = %s",(nota.id,))
            if cursor.fetchone() is None:
                raise ValueError("Nota não encontrada")
            
            cursor.execute(queryStr, values)

    except Exception as ex:
        if hasattr(ex, "args"):
            if ex.args[0] == 1062:
                #Já existe um par nota e prova com outro id.
                raise ValueError("Esse aluno já possui nota para essa prova")
            elif ex.args[0] == 1452:
                #Alguma das chaves estrangeiras não existe
                raise ValueError("Aluno ou prova não existe")
        raise
        
def deletar_nota(id_nota: int) -> None:
    queryStr = """
        DELETE FROM notas WHERE id = %s;
    """

    with ConnectionDB() as cursor:  
        cursor.execute(queryStr, (id_nota,))
        if cursor.rowcount == 0:
            raise ValueError("Nota não encontrada")
