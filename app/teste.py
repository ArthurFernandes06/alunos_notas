from repositores import cadastrar_prova, listar_todas_provas,atualizar_prova, deletar_prova,buscar_prova
from schemas import ProvasSchema
from dotenv import load_dotenv
import os

load_dotenv()

prova = ProvasSchema(id=5, nome="Programação")
print(atualizar_prova(prova))
lista_provas = listar_todas_provas()

for prova in lista_provas:
    print(str(prova.id) + " " +prova.nome)

prova1 = buscar_prova(id=3)
if prova1:
    print(f"Prova buscada: id= {prova1.id} nome= {prova1.nome}")
else:
    print(prova1)