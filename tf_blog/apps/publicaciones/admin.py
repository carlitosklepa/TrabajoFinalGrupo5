from django.contrib import admin
from .models import Publicacion, Categoria, Usuario


admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Usuario)