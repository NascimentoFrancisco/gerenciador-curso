from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,ListView, DeleteView,View
from django.urls import reverse_lazy
# Create your views here.

from .models import Curso

class ListCursos(ListView):
    
    template_name: str = 'curso/list.html'

    def get_queryset(self):
        queryset = Curso.objects.all()
        return queryset
