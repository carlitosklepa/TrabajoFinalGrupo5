from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, null= False)
    resumen = models.CharField(max_length=500, null= False)
    Contenido = models.TextField
    autor = models.ForeignKey("usuarios.usuarios", on_delete = models.CASCADE,)
    categoria = models.ForeignKey("categorias.categorias", on_delete=models.CASCADE, )
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    fecha_de_Edicion = models.DateTimeField(default=timezone.now)
    imagen_usuario = models.ImageField(upload_to="", null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo