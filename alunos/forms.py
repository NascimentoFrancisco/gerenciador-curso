from django import forms
from django.utils import timezone
from curso.models import Curso
from .models import Aluno, CursoAluno

class AlunoCreateForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','data_nascimento','escolaridade']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'data_nascimento': forms.TextInput(attrs= {'class':'form-control','type':'date'}),
            'escolaridade':forms.TextInput(attrs= {'class':'form-control'}),
        }