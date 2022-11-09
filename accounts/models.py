from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .validadores import valida_cpf
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length = 11, unique=True, verbose_name='CPF', 
        error_messages={'unique' : "CPF já cadastrado!"},
        validators = [valida_cpf])
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.cpf