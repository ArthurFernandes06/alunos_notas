from app.repositories import listar_todas_notas, buscar_nota, buscar_notas_aluno, buscar_notas_prova, cadastrar_nota, atualizar_nota, deletar_nota,buscar_nota_prova_aluno
from app.schemas import NotasSchema

from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

@router.get("/notas", status_code=200)
def get_notas(id_aluno: int | None = Query(default=None), id_prova: int | None = Query(default=None)):
    if id_aluno and id_prova:
        nota = buscar_nota_prova_aluno(id_aluno=id_aluno, id_prova=id_prova)
        if nota is None:
            return []
        
        return [nota]
    
    elif id_aluno:
        return buscar_notas_aluno(id_aluno)
    
    elif id_prova:
        return buscar_notas_prova(id_prova)
    
    return listar_todas_notas()

@router.get("notas/{id_nota}")
def get_nota(id_nota: int):
    nota = buscar_nota(id_nota)
    if nota is None:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return nota