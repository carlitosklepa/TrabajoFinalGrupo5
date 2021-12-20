from django import forms
from .models import Comentario

class Comentario_Form(forms.ModelForm):
	Contenido = forms.CharField(label="Contenido del Comentario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su comentario"}))

	class Meta:
		model = Comentario
		fields = ["Contenido"]
