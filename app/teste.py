from repositories import cadastrar_prova, listar_todas_provas, atualizar_prova, buscar_prova, deletar_prova
from schemas import AlunosSchema,ProvasSchema
from dotenv import load_dotenv
import os

load_dotenv()

prova = ProvasSchema(id=2, nome="Lógica")
atualizar_prova(prova)
print(buscar_prova(id=2))
lista_provas = listar_todas_provas()

for prova in lista_provas:
    print(str(prova.id) + " " + prova.nome )

