from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    numero_telefono = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    email = models.EmailField(max_length=254)
    user_name = models.CharField(max_length=50, default="incognito")
    password = models.CharField(max_length=50)
    fecha_de_registro = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100, null=True)
    estado = models.BooleanField(default=True)
    imagen_usuario = models.ImageField(upload_to="", null=True)
    es_administrador = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
