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

    nombre= models.CharField(max_length=25)
    crear_tipo_item = models.BooleanField()
    editar_tipo_item = models.BooleanField()
    eliminar_tipo_item = models.BooleanField()
    crear_linea_base= models.BooleanField()
    abrir_linea_base= models.BooleanField()
    crear_item=models.BooleanField()
    editar_item=models.BooleanField()
    eliminar_item=models.BooleanField()
    aprobar=models.BooleanField()
    revivir=models.BooleanField()
    reversionar=models.BooleanField()
    asignar_padre=models.BooleanField()
    asignar_antecesor=models.BooleanField()
    usuario=models.ManyToManyField(Usuario, related_name='usuario_rol')
    fase = models.ForeignKey(Fase, related_name='fase_rol')

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_rol', kwargs={'pk': self.pk})