from app.repositories import buscar_aluno, buscar_aluno_matricula, cadastrar_aluno, atualizar_aluno, listar_todos_alunos, deletar_aluno
from app.schemas import AlunosSchema
from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

@router.get("/alunos",status_code=200)
def get_alunos(matricula:str | None = Query(default=None)):
    if matricula:
        aluno = buscar_aluno_matricula(matricula)
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        return [aluno] if aluno else []

    return listar_todos_alunos()


@router.get("/alunos/{aluno_id}", status_code=200)
def get_aluno(aluno_id: int):
    aluno = buscar_aluno(aluno_id)

    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    
    return aluno

@router.post("/alunos", status_code=201)
def create_aluno(aluno: AlunosSchema):
    try:
        novo_aluno = cadastrar_aluno(aluno)
    except ValueError as v:
        raise HTTPException(status_code=409, detail=str(v))
    
    return novo_aluno

@router.put("/alunos/{aluno_id}",status_code=201)
def update_aluno(aluno: AlunosSchema, aluno_id: int):
    aluno.id = aluno_id
    
    try:
        atualizar_aluno(aluno)
    except ValueError as v:
        if str(v).lower() == "aluno não encontrado":
            raise HTTPException(status_code=404, detail=str(v))
        else:
            raise HTTPException(status_code=409, detail=str(v))
    
    return aluno

@router.delete("/alunos/{aluno_id}",status_code=204)
def delete_aluno(aluno_id):
    try:
        deletar_aluno(id)
    except ValueError as v:
        raise HTTPException(status_code=404, detail=str(v))