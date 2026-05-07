from app.repositories import *
from app.schemas import *

aluno1 = buscar_aluno_matricula("01A")
aluno2 = buscar_aluno_matricula("01B")

atualizar_nota(NotasSchema(id=20,id_prova=2, id_aluno=1, nota=9.6))

for nota in listar_todas_notas():
    aluno = buscar_aluno(nota.id_aluno)
    prova = buscar_prova(nota.id_prova)
    print(f"O aluno {aluno.nome} fez a prova {prova.nome} e tirou a nota {nota.nota}, id={nota.id}")