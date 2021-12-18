from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.publicaciones.models import Publicacion
from apps.usuarios.models import Usuario
from django.views.generic import ListView


class Inicio(ListView):
    template_name="inicio.html"
    model = Publicacion
    context_object_name="publicaciones"

    def get_queryset(self):
        return Publicacion.objects.filter(guardar_como_borrador=False) and Usuario.objects.filter(tipo__in=[2])
'''

class Inicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["publicaciones"] = Publicacion.objects.all()
        return context
'''


class Contacto(TemplateView):
    template_name = "contacto.html"

class Ingresar(TemplateView):
    template_name = "ingresar.html"


class Registrarte(TemplateView):
    template_name = "registrarte.html"


class Post(TemplateView):
    template_name = "post.html"

class Registro(TemplateView):
    template_name = "registro.html"

def ods(request):
    return render(request, "ods.html")
