from django.db import models
from django.utils import timezone

class Comentario(models.Model):
    Contenido = models.CharField(max_length=500, null=False)
    autor = models.ForeignKey("usuarios.usuario", on_delete=models.CASCADE, )
    fecha_publicacion = models.DateTimeField,
    post_comentado = models.ForeignKey("publicaciones.publicacion", on_delete=models.CASCADE, )

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()
