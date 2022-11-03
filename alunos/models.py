from django.db import models
from django.conf import settings
from django.utils import timezone
from curso.models import Curso
from django.core.exceptions import ValidationError
# Create your models here.

now = timezone.now()


class Aluno(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    escolaridade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class CursoAluno(models.Model):
    aluno = models.ForeignKey(Aluno,on_delete= models.PROTECT)#Mudar o ralcionamento para 1:1
    curso = models.ForeignKey(Curso,on_delete= models.PROTECT)#
    data_matricula = models.DateField(default = now.date())

    def __str__(self):
        return self.curso.titulo

