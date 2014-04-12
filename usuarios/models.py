__author__ = 'penagonzalez'

from django.db import models

# Create your models here.


# class Roles (models.Model):


class Usuarios (models.Model):


    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    password=models.CharField(max_length=20, null=False)
    cedula=models.PositiveIntegerField(max_length=10, null=False, default=0)
    email=models.EmailField(max_length=20)
    estado=models.BooleanField(default=True)
    num_telefono=models.CharField(max_length=15)
    direccion=models.CharField(max_length=50)
    observacion=models.CharField(max_length=50)
   # permiso=models.ManyToManyField(Roles)

    def __unicode__(self):
        return self.nombre
