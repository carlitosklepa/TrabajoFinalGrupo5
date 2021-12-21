from django.shortcuts import render

# Create your views here.

from django.urls               import reverse_lazy
from django.views.generic      import  CreateView

from .forms  import Usuario_Form
from .models import Usuario

class Registrarte(CreateView):
	template_name = "registrarte.html"
	model = Usuario
	form_class = Usuario_Form

	def get_success_url(self, **kwargs):
		return reverse_lazy("ingresar")