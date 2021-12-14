from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=50, null=False)
    numero_telefono = models.DecimalField(max_digits=15, decimal_places=0)
    email = models.EmailField (null = False)
    user_name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    fecha_de_registro = models.CharField(max_length=50, null=False)
    tipo = models.CharField(max_length=100, null=False)
    estado = models.BooleanField,
    imagen_usuario = models.ImageField(upload_to="", null=True)

    def __str__(self):
        return self.user_name