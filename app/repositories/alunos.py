from app.schemas import AlunosSchema
from app.core import ConnectionDB

def listar_todos_alunos() -> list[AlunosSchema]:
    #Retorna uma lista de com objetos AlunosSchema.
    queryStr = """
        SELECT id, matricula, nome, turma FROM alunos;
    """
    lista_alunos = list()
    with ConnectionDB() as cursor:
        cursor.execute(queryStr)
        results = cursor.fetchall()

        for result in results:
            aluno = AlunosSchema(
                id= result[0],
                matricula = result[1],
                nome= result[2],
                turma= result[3]
            )
            lista_alunos.append(aluno)


    return lista_alunos

def buscar_aluno(id: int) -> AlunosSchema | None:
    queryStr = """
        SELECT id, matricula, nome, turma FROM alunos
        WHERE id = %s;
    """
    with ConnectionDB() as cursor:
        cursor.execute(queryStr, (id,))
        result = cursor.fetchone()

        if result:
            aluno = AlunosSchema(
                id=result[0],
                matricula= result[1],
                nome = result[2],
                turma = result[3]
            )
        else:
            aluno = None

    return aluno

def buscar_aluno_matricula(matricula: str) -> AlunosSchema | None:
    queryStr = """
        SELECT id, matricula, nome, turma FROM alunos
        WHERE matricula = %s;
    """
    with ConnectionDB() as cursor:
        cursor.execute(queryStr, (matricula,))
        result = cursor.fetchone()

        if result:
            aluno = AlunosSchema(
                id = result[0],
                matricula = result[1],
                nome = result[2],
                turma = result[3]
            )
        else:
            aluno = None

    return aluno

def cadastrar_aluno(aluno: AlunosSchema) -> AlunosSchema:
    queryStr = """
        INSERT INTO alunos (matricula, nome, turma)
        VALUES (%s, %s, %s);
    """
    values = (aluno.matricula, aluno.nome, aluno.turma,)
    try:
        with ConnectionDB() as cursor:
            cursor.execute(queryStr, values)
            aluno.id = cursor.lastrowid
    except Exception as ex:
        if hasattr(ex, "args") and ex.args[0] == 1062:
            raise ValueError("Essa matricula já existe.")
        else:
            raise

    return aluno


def atualizar_aluno(aluno: AlunosSchema) -> None:
    queryStr = """
        UPDATE alunos 
        SET nome = %s, matricula = %s, turma = %s 
        WHERE id = %s;
    """
    values = (aluno.nome, aluno.matricula, aluno.turma, aluno.id,)
    if aluno.id is None:
        raise ValueError("Requisição sem id.")
    try:
        with ConnectionDB() as cursor:
            cursor.execute(queryStr, values)
            if cursor.rowcount == 0:
                raise ValueError("Aluno não encontrado.")
    except Exception as ex:
        if hasattr(ex, "args") and ex.args[0] == 1062:
            raise ValueError("Matricula já cadastrada")
        else:
            raise

def deletar_aluno(id: int) -> None:
    queryStr = """
        DELETE FROM alunos WHERE id = %s;
    """
    with ConnectionDB() as cursor:
        cursor.execute(queryStr,(id,))
        if cursor.rowcount == 0:
            raise ValueError("Aluno não encontrado.")
