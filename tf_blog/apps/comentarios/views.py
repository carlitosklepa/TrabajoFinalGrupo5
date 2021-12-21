from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
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


class ListarComentarios(ListView):
	template_name="comentarios/lista_comentarios.html"
	model = Comentario
	context_object_name="comentarios"
	#paginate_by = 10

	def get_queryset(self):
		post_comentado = get_object_or_404(Publicacion, pk=self.kwargs.get('id_publicacion'))
		return Comentario.objects.filter(post_comentado=post_comentado).order_by('fecha_publicacion')

'''
def get_queryset(self):
	self.request
	return Comentario.objects.filter(post_comentado=self.request.post_comentado).order_by("fecha_publicacion")
'''
