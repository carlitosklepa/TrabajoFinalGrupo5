from django.urls import path
from . import views

app_name = "comentarios"

urlpatterns = [
	path("nuevo_comentario/<int:id_publicacion>/", views.Nuevo_Comentario.as_view(), name="nuevo_comentario"),
]
