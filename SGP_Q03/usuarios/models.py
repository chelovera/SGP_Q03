# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""

from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

"""
Django usuarios/models

"""

class Usuario(User):

    """ Estos son los campos que contiene usuarios/models.py

    @param nombre : Es el nombre del usuario, es un campo obligatorio
    @type nombre : models.CharField(max_length=50, null=False)

    @param apellido : Es el nombre del usuario, es un campo obligatorio
    @type apellido : models.CharField(max_length=50, null=False)

    @param telefono : es el telefono de contacto del usuario
    @type telefono : models.PositiveIntegerField(default=0)

    @param cedula : es el documento de identidad del usuario
    @type cedula : models.PositiveIntegerField(default=0)

    @param direccion: en este campo se indica la direccion del usuario
    @type direccion : models.CharField(max_length=50, null=False, blank=True)

    @param estado: indica que el usuario puede estar en estado Activo o Inactivo
    @type estado : models.BooleanField(default=True)

    """

    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    telefono = models.PositiveIntegerField(default=0, blank=True)
    cedula = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=50, null=False, blank=True)


    def __unicode__(self):
        return self.nombre+str(self.codigo)

    def get_absolute_url(self):
        return reverse('editar_usuario', kwargs={'pk': self.pk})


