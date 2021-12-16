"""tf_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio.as_view(), name = "inicio"),
    path('contacto/', views.Contacto.as_view, name = "contacto"),
    path('ingresar/', views.Ingresar.as_view, name = "ingresar"),
    path('registrarte/', views.Registrarte.as_view, name = "registrarte"),
    path('ods/', views.ods, name = "ods"),
    path('post/', views.Post.as_view, name = "post")
]
