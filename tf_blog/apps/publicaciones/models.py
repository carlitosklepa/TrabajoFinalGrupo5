from django.db import models
from apps.usuarios.models import Usuario
from django.utils import timezone

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, default='')
    resumen = models.CharField(max_length=500, default='')
    Contenido = models.TextField(default="")
    autor = models.ForeignKey("usuarios.usuario", on_delete = models.CASCADE)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    fecha_de_Edicion = models.DateTimeField(default=timezone.now)
    imagen_publicacion = models.ImageField(upload_to="publicaciones", null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
