from django.db import models

class Publicacion(models.Model):
    atributo_str = models.CharField(max_length=255)
    atributo_decimal = models.DecimalField(max_digits=9, decimal_places=2)
