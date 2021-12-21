from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Usuario

class Usuario_Form(UserCreationForm):
	username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre de usuario"}))
	# attrs={'cols': 80, 'rows': 20}
	first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre"}))
	last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese apellido"}))
	#password = forms.CharField(widget=forms.PasswordInput())
	#password_2 = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Usuario
		fields = ["first_name", "last_name", "numero_telefono", "email", "username","imagen_usuario"]
