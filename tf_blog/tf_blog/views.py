from django.shortcuts import render

from django.views.generic.base import TemplateView


class Inicio(TemplateView):
    template_name = "inicio.html" 


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




    
