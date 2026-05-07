from app.repositories import listar_todas_provas, buscar_prova, cadastrar_prova, atualizar_prova, deletar_prova
from app.schemas import ProvasSchema
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/provas", status_code=200, response_model=list[ProvasSchema])
def get_provas():
    return listar_todas_provas()

@router.get("/provas/{id_prova}", status_code=200, response_model=ProvasSchema)
def get_prova(id_prova: int):
    prova = buscar_prova(id_prova)

    if prova is None:
        raise HTTPException(status_code=404, detail="Prova não encontrada.")
    
    return prova

@router.post("/provas",status_code=201,response_model=ProvasSchema)
def create_prova(prova: ProvasSchema):
    return cadastrar_prova(prova)

@router.put("/provas/{id_prova}",status_code=200, response_model=ProvasSchema)
def update_prova(id_prova: int, prova: ProvasSchema):
    prova.id = id_prova
    try:
        atualizar_prova(prova)
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return prova

@router.delete("/provas/{id_prova}",status_code=204)
def delete_prova(id_prova: int):
    try:
        deletar_prova(id_prova)
    except ValueError as ex:
        raise HTTPException(status_code=404, detail=str(ex))