from django.shortcuts import render


def inicio(request):
    return render(request, "inicio.html")

def contacto(request):
    return render(request, "contacto.html")

def ingresar(request):
    return render(request, "ingresar.html")

def registrarte(request):
    return render(request, "registrarte.html")

def ods(request):
    return render(request, "ods.html")

def post(request):
    return render(request, "post.html")
