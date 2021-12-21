from django.urls import path
from . import views

app_name = "comentarios"

urlpatterns = [
	path("nuevo_comentario/<int:id_publicacion>/", views.Nuevo_Comentario.as_view(), name="nuevo_comentario"),

	#path('ListarComentarios/', views.mis_favoritos, name="listar_comentarios"),

	path('ListarComentarios/<int:id_publicacion>/', views.ListarComentarios.as_view(), name="listar_comentarios"),

	path("admin/eliminar/<int:pk>/", views.EliminarC_Admin.as_view(), name="admin_eliminar")
]
