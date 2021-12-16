from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField
 
# Create your models here.
class Usuario_Administrador(BaseUserManager):
    def crear_usuario(self, nombre, apellido,edad=None,username,email,password)
        if not email:
            raise ValueError('Para crear un usuario es necesario el email')
        if not nombre:
            raise ValueError('Para completar el registro, es necesario que ingrese su nombre...')
        if not apellido:
             raise ValueError('Para completar el registro, es necesario que ingrese su apellido...')
        if not edad:
            raise ValueError('Para completar el registro, es necesario que ingrese su edad...')
        if not username:
            raise ValueError('Para completar el registro, es necesario que ingrese su usuario...')
        if not password:
            raise ValueError('Para completar el registro, es necesario que ingrese su contraseña..')
        usuario=self.model(
            nombre=nombre
            apellido=apellido
            edad=edad
            username=username
            email=self.normalize_email(email)
         )      
        usuario.set_password(password)
        usuario.save()
        return usuario
    def crear_superuser(self,nombre,apellido,edad,username,password):
        usuario=self.crear_usuario(
            nombre=nombre
            apellido=apellido
            edad=edad
            username=username
            email=email
            password=password
        )



        
      
class Usuario_registrado(AbstractBaseUser):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.DateField()
    email=EmailField(max_length=70)
    username=models.CharField('Nombre de usuario:' unique=True, max_length=100)
    nro_celular=models.CharField('Numero de tefono', max_length=100)
    usuario_activo=models.BooleanField(default=True)
    usuario_admin=models.BooleanField(default=False)

    USERNAME_FIELDS='username'
    REQUIERED_FIELDS=['email','nombres','apellido','edad']


