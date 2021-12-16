from django.db import models
from django.utils import timezone

class Comentario(models.Model):
    Contenido = models.CharField(max_length=500, default='')
    autor = models.ForeignKey("usuarios.usuario", on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    post_comentado = models.ForeignKey("publicaciones.publicacion", on_delete=models.CASCADE, null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()
