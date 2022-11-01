from django.urls import path
from .views import ListCursos

app_name = "cursos"

urlpatterns = [
    path('list/', ListCursos.as_view(), name='list_curso'),       
]