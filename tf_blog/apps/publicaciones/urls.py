from django.urls import path

from . import views

app_name = "publicaciones"

urlpatterns = [
	path("post/<int:pk>/", views.Post.as_view(), name="post"),
	path("nuevo/", views.NuevaP.as_view(), name="nuevo"),
	path("listar/", views.ListarP.as_view(), name="listar"),

	# Admin
	#path("admin/listar/", views.ListarP_Admin.as_view(), name="admin_listar"),
	path("admin/menu/", views.MenuP.as_view(), name="admin_menu"),
	path("admin/editar/<int:pk>/", views.EditarP_Admin.as_view(), name="admin_editar"),
	path("admin/eliminar/<int:pk>/", views.EliminarP_Admin.as_view(), name="admin_eliminar"),

	#-- la carpeta--path("MisPublicaciones/", views.MisPublicaciones.as_view(), name="mis_publicaciones")
]
