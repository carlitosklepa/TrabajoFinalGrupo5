from django.urls import path 

from . import views

app_name = "publiaciones"

urlpatterns = [
	#path("Detalle/<int:pk>/", views.Detalle.as_view(), name="detalle"),

	# Admin
	path("Admin/Registro/", views.Registro.as_view(), name="registro"),
	#path("Admin/Nuevo/", views.NuevaP_Admin.as_view(), name="admin_nuevo"),
	#path("Admin/Editar/<int:pk>/", views.EditarP_Admin.as_view(), name="admin_editar"),

	#-- la carpeta--path("MisPublicaciones/", views.MisPublicaciones.as_view(), name="mis_publicaciones")

]