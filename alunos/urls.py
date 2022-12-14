from django.urls import path
from .views import (AlunoCreate, CursoAlunoCreate, HomeAluno, CursoAlunoList, 
    CursoAlunoDelete, CursoAlunoListPorCurso)

app_name = "alunos"

urlpatterns = [
    path('', HomeAluno.as_view(), name='home_aluno'),
    path('create/', AlunoCreate.as_view(), name='create_aluno'),
    path('matricula/', CursoAlunoCreate.as_view(), name='aluno_matricula'),
    path('list-curso-aluno/',CursoAlunoList.as_view(),name='list_curso_aluno'),
    path('list-aluno-curso/<int:pk>/',CursoAlunoListPorCurso.as_view(),name='list_aluno_curso'),
    path('sair-curso/<int:pk>/',CursoAlunoDelete.as_view(),name='sair_curso'),       
]