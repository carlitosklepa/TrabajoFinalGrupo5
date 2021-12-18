from django.urls import path

from . import views

app_name = "publicaciones"

urlpatterns = [
	path("post/<int:pk>/", views.Post.as_view(), name="post"),
	path("nuevo/", views.NuevaP.as_view(), name="nuevo"),

	# Admin
	path("admin/listar/", views.ListarP_Admin.as_view(), name="admin_listar"),
	path("admin/nuevo/", views.NuevaP_Admin.as_view(), name="admin_nuevo"),
	path("admin/editar/<int:pk>/", views.EditarP_Admin.as_view(), name="admin_editar"),

	#-- la carpeta--path("MisPublicaciones/", views.MisPublicaciones.as_view(), name="mis_publicaciones")
]
