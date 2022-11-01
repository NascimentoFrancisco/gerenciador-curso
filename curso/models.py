from django.db import models
from monitores.models import Monitor

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length = 255,verbose_name='Título')
    minitores = models.ManyToManyField(Monitor,verbose_name="Monitores")
    carga_horaria = models.IntegerField(verbose_name='Carga horária')
    data = models.DateField()
    numero_vagas = models.IntegerField(verbose_name='Quantidade de vagas')
    prublco_alvo = models.CharField(max_length = 255,verbose_name='Público alvo')
    inicio_matriculas = models.DateTimeField(verbose_name='Início das matrículas')
    fim_matriculas = models.DateTimeField(verbose_name='Encerramento das matrículas')

    def __str__(self):
        return self.titulo