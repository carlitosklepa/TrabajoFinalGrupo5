from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class Usuario_Form(UserCreationForm):
	user_name = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre de usuario"}))
	# attrs={'cols': 80, 'rows': 20}
	nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese nombre"}))
	apellido = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese apellido"}))
	#password = forms.CharField(widget=forms.PasswordInput())
	#password_2 = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Usuario
		fields = ["nombre", "apellido", "numero_telefono", "email", "user_name"]
