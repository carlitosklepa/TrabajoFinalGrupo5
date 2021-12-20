from django import forms

from .models import Publicacion

class Publicacion_Form(forms.ModelForm):
	titulo = forms.CharField(label="Titulo de la Publicación", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese titulo de la publicación"}))
	#resumen = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
	#contenido = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

	class Meta:
		model = Publicacion
		fields = ["titulo", "resumen", "Contenido", "categorias", "imagen_publicacion", "guardar_como_borrador"]
