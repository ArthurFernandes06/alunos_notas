from app.routers import router_provas,router_alunos, router_notas
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_provas)
app.include_router(router_alunos)
app.include_router(router_notas)

@app.get("/")
def get_main():
    return {"Mensagem": "Bem vindo !!"}