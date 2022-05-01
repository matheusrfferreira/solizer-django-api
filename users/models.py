from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPES = [
    (1, 'Client'),
    (2, 'Integrator')
]


class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=False)
    cell_phone_number = models.CharField(max_length=255, blank=False)
    picture_url = models.URLField(blank=True)
    cpf = models.CharField(max_length=11, blank=False)
    cnpj = models.CharField(max_length=14, blank=True)
    user_type = models.SmallIntegerField()
