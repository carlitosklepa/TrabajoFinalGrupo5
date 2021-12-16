from django.urls import path

from . import views

app_name = "publicaciones"

urlpatterns = [
	path("post/<int:pk>/", views.Post.as_view(), name="post"),

	# Admin
	path("Admin/Listar/", views.ListarP_Admin.as_view(), name="admin_listar"),
	path("Admin/Nuevo/", views.NuevaP_Admin.as_view(), name="admin_nuevo"),
	path("Admin/Editar/<int:pk>/", views.EditarP_Admin.as_view(), name="admin_editar"),

	#-- la carpeta--path("MisPublicaciones/", views.MisPublicaciones.as_view(), name="mis_publicaciones")
]
