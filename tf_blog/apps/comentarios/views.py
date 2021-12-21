from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Comentario
from apps.usuarios.models import Usuario
from apps.publicaciones.models import Publicacion
from .forms  import Comentario_Form
from django.contrib.auth.mixins import LoginRequiredMixin


class Nuevo_Comentario(LoginRequiredMixin, CreateView):
	template_name = "comentarios/nuevo_comentario.html"
	model = Comentario
	form_class = Comentario_Form

	def get_success_url(self, **kwargs):
		return reverse_lazy("publicaciones:post", kwargs={"pk": self.kwargs["id_publicacion"]})

	def form_valid(self, form):
		f = form.save(commit=False)
		f.autor_id = self.request.user.id
		f.post_comentado = Publicacion.objects.get(id=self.kwargs["id_publicacion"])
		return super(Nuevo_Comentario, self).form_valid(form)
