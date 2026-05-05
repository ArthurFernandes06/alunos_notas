from app.routers import router_provas,router_alunos
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_provas)
app.include_router(router_alunos)

@app.get("/")
def get_main():
    return {"Mensagem": "Bem vindo !!"}