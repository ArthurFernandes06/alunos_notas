from app.repositories import listar_todas_provas, buscar_prova, cadastrar_prova, atualizar_prova, deletar_prova
from app.schemas import ProvasSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/provas", status_code=200)
def get_provas():
    return listar_todas_provas()

@router.get("/provas/{id}", status_code=200)
def get_prova(id: int):
    prova = buscar_prova(id)

    if prova is None:
        raise HTTPException(status_code=404, detail="Prova não encontrada.")
    
    return {"id": prova.id, "nome" : prova.nome}

@router.post("/provas",status_code=201)
def create_prova(prova: ProvasSchema):
    nova_prova = cadastrar_prova(prova)
    return {"id": nova_prova.id, "nome": nova_prova.nome}

@router.put("/provas/{id}",status_code=200)
def update_prova(id: int, prova: ProvasSchema):
    prova.id = id
    try:
        atualizar_prova(prova)
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return {"id": prova.id, "nome": prova.nome}

@router.delete("/provas/{id}",status_code=204)
def delete_prova(id: int):
    try:
        deletar_prova(id)
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))