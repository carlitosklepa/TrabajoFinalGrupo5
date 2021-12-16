from django.http import request
from django.shortcuts import render

# Create your views here.
def login_autenticar():
    return render(request,'templates/ingresar2.html')