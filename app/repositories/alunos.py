from app.schemas import AlunosSchema
from app.core import ConnectionDB

def listar_todos_alunos() -> list[AlunosSchema]:
    #Retorna uma lista de com objetos AlunosSchema.
    queryStr = """
        SELECT id, matricula, nome, turma FROM alunos;
    """
    lista_alunos = list()
    with ConnectionDB() as cursor:
        try:
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
        except Exception as ex:
            print(ex)

    return lista_alunos

def buscar_aluno(id: int) -> AlunosSchema:
    pass

def buscar_aluno_matricula(matricula: str) -> AlunosSchema:
    pass

def cadastrar_aluno(aluno: AlunosSchema) -> bool:
    queryStr = """
        INSERT INTO alunos (matricula, nome, turma)
        VALUES (%s, %s, %s);
    """
    sucess_operation = False
    values = (aluno.matricula, aluno.nome, aluno.turma,)
    with ConnectionDB() as cursor:
        try:
            cursor.execute(queryStr, values)
            sucess_operation = True
        except Exception as ex:
            print(ex)
            
    return sucess_operation


def atualizar_aluno(aluno: AlunosSchema) -> bool:
    pass

def deletar_aluno(aluno: AlunosSchema) -> bool:
    pass
