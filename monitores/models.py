from django.db import models
from django.conf import settings
# Create your models here.

class Monitor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    capacitacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

