from django.db import models
from django.contrib.auth.models import AbstractUser

TIPO_CHOICES = (
    (1, "Lector"),
    (2, "Escritor")
)

class Usuario(AbstractUser):
    numero_telefono = models.DecimalField(max_digits=15, decimal_places=0, null=True)

    tipo = models.IntegerField(choices=TIPO_CHOICES, default=1)

    imagen_usuario = models.ImageField(upload_to="usuarios", null=True)

    es_administrador = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name()
