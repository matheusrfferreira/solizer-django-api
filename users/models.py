from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import IntEnum


class UserTypes(IntEnum):
    CLIENT = 1
    INTEGRATOR = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=False)
    cell_phone_number = models.CharField(max_length=255, blank=False)
    picture_url = models.URLField(blank=True)
    cpf = models.CharField(max_length=11, blank=False)
    cnpj = models.CharField(max_length=14, blank=True)
    user_type = models.IntegerField(choices=UserTypes.choices(), default=UserTypes.CLIENT)
    


