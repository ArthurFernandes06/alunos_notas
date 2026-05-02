from repositores import cadastrar_prova
from schemas import ProvasSchema
from dotenv import load_dotenv
import os

load_dotenv()
prova = ProvasSchema(nome= "Matemática")
print(cadastrar_prova(prova))