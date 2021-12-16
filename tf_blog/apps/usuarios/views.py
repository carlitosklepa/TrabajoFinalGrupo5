from django.shortcuts import render

# Create your views here.

from django.urls               import reverse_lazy
from django.views.generic      import ListView, CreateView

from .forms  import Usuario_Form
from .models import Usuario

class Registro(CreateView):
	template_name = "registro.html"
	model = Usuario
	form_class = Usuario_Form

	def get_success_url(self, **kwargs):
		return reverse_lazy("registro")