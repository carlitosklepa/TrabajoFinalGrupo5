from django import forms

from . models import Publicacion, Categoria

class Publicacion_Form(forms.ModelForm):
	titulo = forms.CharField(label="Titulo de la Publicación", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese titulo de la publicación"}))
	#resumen = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
	#contenido = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

	class Meta:
		model = Publicacion
		fields = ["titulo", "resumen", "Contenido", "categorias", "imagen_publicacion", "guardar_como_borrador"]

class PublicacionFiltroForms(forms.Form):
	titulo = forms.CharField(required=False)
	categorias = forms.ModelChoiceField(queryset=Categoria.objects.all())

	def __init__(self, *args, **kwargs):
		super(PublicacionFiltroForms, self).__init__(*args, **kwargs)
		self.fields['categorias'].required = False
