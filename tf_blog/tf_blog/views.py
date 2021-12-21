from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.publicaciones.models import Publicacion
from apps.usuarios.models import Usuario
from django.views.generic import ListView
from apps.publicaciones.forms  import Publicacion_Form, PublicacionFiltroForms


class Inicio(ListView):
    template_name="inicio.html"
    model = Publicacion
    context_object_name="publicaciones"

'''
    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        busqueda_titulo = self.request.GET.get("titulo", None)
        busqueda_categoria = self.request.GET.get("categorias", None)
        context["form_filtro"] = PublicacionFiltroForms(initial={'titulo': busqueda_titulo, "categorias":(busqueda_categoria)})
        return context

    def get_queryset(self):
        busqueda_titulo = self.request.GET.get("titulo", None)
        busqueda_categoria = self.request.GET.get("categorias", None)
        query = Publicacion.objects.all().order_by("titulo")
        if busqueda_titulo is not None and busqueda_titulo != "":
            query = query.filter(titulo__icontains=busqueda_titulo)
        if busqueda_categoria is not None and busqueda_categoria != "":
            query = query.filter(categorias=busqueda_categoria)
        return query



    def get_queryset(self):
        return Publicacion.objects.filter(guardar_como_borrador=False) and Usuario.objects.filter(tipo__in=[2])
    '''



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

class Ods(TemplateView):
   template_name = "ods.html"
