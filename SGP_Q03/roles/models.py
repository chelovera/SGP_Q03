# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""

from django.core.urlresolvers import reverse
from django.db import models
from usuarios.models import Usuario
from fases.models import Fase

""" MODEL/ROL
Estos campos representan los permisos que se podran utilizar dentro de cada Proyecto.
@param crear_tipo_item
@type models.BooleanField

@param editar_tipo_item
@type models.BooleanField

@param eliminar_tipo_item
@type models.BooleanField

@param crear_linea_base
@type models.BooleanField

@param abrir_linea_base
@type models.BooleanField

@param crear_item
@type models.BooleanField

@param editar_item
@type models.BooleanField

@param eliminar_item
@type models.BooleanField


@param aprobar
@type models.BooleanField

@param revivir
@type models.BooleanField

@param reversionar
@type models.BooleanField

@param asignar_padre
@type models.BooleanField

@param asignar_antecesor
@type models.BooleanField

@param miembros
@type models.BooleanField
"""

class Rol(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    #usuario=models.ForeignKey(Usuario, related_name='usuario_rol')      #!!!
    fase = models.ForeignKey(Fase, related_name='fase')
    #usuario=models.ManyToManyField(Usuario, related_name='usuario', blank=True, null=True)
    crear_tipo_item = models.NullBooleanField(null=True, blank=True)
    editar_tipo_item = models.NullBooleanField(null=True, blank=True)
    eliminar_tipo_item = models.NullBooleanField(null=True, blank=True)
    crear_linea_base = models.NullBooleanField(null=True, blank=True)
    abrir_linea_base = models.NullBooleanField(null=True, blank=True)
    crear_item = models.NullBooleanField(null=True, blank=True)
    editar_item=models.NullBooleanField(null=True, blank=True)
    eliminar_item=models.NullBooleanField(null=True, blank=True)
    aprobar=models.NullBooleanField(null=True, blank=True)
    revivir=models.NullBooleanField(null=True, blank=True)
    reversionar=models.NullBooleanField(null=True, blank=True)
    asignar_padre=models.NullBooleanField(null=True, blank=True)
    asignar_antecesor=models.NullBooleanField(null=True, blank=True)
    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_rol', kwargs={'pk': self.pk})


class RolAsignar (models.Model):
    codigo = models.AutoField(primary_key=True)
    #usuarios = models.ManyToManyField(Usuario)
    usuario = models.ForeignKey(Usuario)
    rol = models.ForeignKey(Rol)
    confirmar = models.BooleanField(max_length=50)

    def __unicode__(self):
        return self.codigo