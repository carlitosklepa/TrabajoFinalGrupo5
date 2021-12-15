from django import forms

from . models import Publicacion

class Publicacion_Form(forms.ModelForm):
	titulo = forms.CharField(label="Titulo de la Publicación", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese titulo de la publicación"}))
	# attrs={'cols': 80, 'rows': 20}
	contenido = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

	class Meta:
		model = Publicacion
		fields = ["titulo", "resumen","Contenido", "imagen", "categoria", ]