from app.repositories import cadastrar_aluno, listar_todos_alunos, buscar_aluno, buscar_aluno_matricula, atualizar_aluno, deletar_aluno
from app.schemas import AlunosSchema
from dotenv import load_dotenv
import os

load_dotenv()

aluno1 = AlunosSchema(matricula="224", nome="Betinaldo", turma="Fisica")
aluno2 = AlunosSchema(matricula="225", nome="Caio Lucas", turma="Computaria")

cadastrar_aluno(aluno1)
cadastrar_aluno(aluno2)

lista_alunos = listar_todos_alunos()
for alu in lista_alunos:
    print(alu)

