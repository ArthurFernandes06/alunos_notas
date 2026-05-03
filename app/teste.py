from app.repositories import cadastrar_prova, listar_todas_provas, atualizar_prova, buscar_prova, deletar_prova
from app.schemas import AlunosSchema,ProvasSchema
from dotenv import load_dotenv
import os

load_dotenv()

prova = ProvasSchema(nome="Lógica")
cadastrar_prova(prova)

lista_provas = listar_todas_provas()
for prova in lista_provas:
    print(str(prova.id) + " " + prova.nome )

