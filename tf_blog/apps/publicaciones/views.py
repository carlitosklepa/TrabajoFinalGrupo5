#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.shortcuts            import render
from django.urls                 import reverse_lazy
from django.views.generic        import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit   import UpdateView

from django.views.generic.edit   import DeleteView

from apps.core.mixins import AdminRequiredMixins

from .forms  import Publicacion_Form
from .models import Publicacion

"""
def detalle(request):
	context = {}
	return render(request, "publicaciones/detalle.html", context)
"""

class ListarP_Admin(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="publicaciones/admin/listar.html"
	model = Publicacion
	context_object_name="publicaciones"
	# permisos_requeridos = ["add_users"]
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(ListarP_Admin, self).get_context_data(**kwargs)
		context["titulo_buscada"] = self.request.GET.get("titulo_publicacion", "")
		return context

	def get_queryset(self):
		busqueda_titulo = self.request.GET.get("titulo_publicacion", "")
		query = Publicacion.objects.all().order_by("titulo")
		if len(busqueda_titulo) > 0:
			query = query.filter(titulo__icontains=busqueda_titulo)
		return query


class MisPubl(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name = "publicaciones/admin/listar.html"
	model = Publicacion
	context_object_name = "publicaciones"

	def get_queryset(self):
		self.request
		return Publicacion.objects.filter(usuario_id=self.request.user.id).order_by("id")

class NuevaP_Admin(CreateView):
	template_name = "publicaciones/admin/nuevo.html"
	model = Publicacion
	form_class = Publicacion_Form

	def get_success_url(self, **kwargs):
		return reverse_lazy("publicaciones:admin_listar")

	def form_valid(self, form):
		f = form.save(commit=False)
		f.autor_id = self.request.user.id
		return super(NuevaP_Admin, self).form_valid(form)


class EditarP_Admin(UpdateView):
	template_name = "publicaciones/admin/editar_p.html"
	model = Publicacion
	form_class = Publicacion_Form
	#context_object_name = "publicacion"

	def get_success_url(self, **kwargs):
		return reverse_lazy("publicaciones:admin_listar")

#class EliminarP_Admin(DeleteView):

class Post(DetailView):
	template_name = "publicaciones/post.html"
	model = Publicacion

class NuevaP(LoginRequiredMixin, CreateView):
	template_name = "pubicaciones/nuevo.html"
	model = Publicacion
	form_class = Publicacion_Form

	def get_success_url(self, **kwargs):
		return reverse_lazy("publicaciones:admin_listar")

	def form_valid(self, form):
		f = form.save(commit=False)
		f.autor_id = self.request.user.id
		return super(NuevaP_Admin, self).form_valid(form)
