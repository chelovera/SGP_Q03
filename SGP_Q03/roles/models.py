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
from proyectos.models import Proyecto

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
    crear_tipo_item = models.BooleanField(default=False)
    editar_tipo_item = models.BooleanField(default=False)
    eliminar_tipo_item = models.BooleanField(default=False)
    crear_linea_base = models.BooleanField(default=False)
    abrir_linea_base = models.BooleanField(default=False)
    crear_item = models.BooleanField(default=False)
    editar_item=models.BooleanField(default=False)
    eliminar_item=models.BooleanField(default=False)
    aprobar=models.BooleanField(default=False)
    revivir=models.BooleanField(default=False)
    reversionar=models.BooleanField(default=False)
    asignar_padre=models.BooleanField(default=False)
    asignar_antecesor=models.BooleanField(default=False)
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
    proyecto = models.ForeignKey(Proyecto)

    def __unicode__(self):
        return self.usuario.nombre + self.rol.nombre+str(self.proyecto)