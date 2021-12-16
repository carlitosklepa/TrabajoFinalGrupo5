from django.db import models
from django.utils import timezone

class Comentario(models.Model):
    contenido = models.CharField(max_length=500)
    autor = models.ForeignKey("usuarios.usuario", on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(blank=False)
    post_comentado = models.ForeignKey("publicaciones.publicacion", on_delete=models.CASCADE)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()
