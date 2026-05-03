from app.routers import router_provas
from fastapi import FastAPI

app = FastAPI()
app.include_router(router_provas)
@app.get("/")
def get_main():
    return {"Mensagem": "Bem vindo !!"}