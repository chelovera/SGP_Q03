# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""
from django.core.urlresolvers import reverse
from django.db import models
from proyectos.models import Proyecto
from datetime import date

"""
Django fases/models

"""


class Fase(models.Model):
    """ Estos son los campos que contiene fase/models.py
    @param codigo: Es el primary key, se genera automaticamente
    @type codigo: models.AutoField(primary_key= True)

    @param nombre: Es el nombre de la fase
    @type nombre: models.CharField(max_length=50)

    @param descripcion: en este campo se indican las caracteristicas mas resaltantes de la fase
    @type descripcion : models.CharField(max_length=200)


    @param estado: indica que la fase puede ser Abierta o Cerrada
    @type estado: models.CharField(max_length=7, choices=ESTADOS, default='Abierta')

    @param fecha_ini: es la fecha de inicio de la fase
    @type fecha_ini: models.DateField(null=True)

    @param fecha_fin:  es la fecha de finalizacion de la fase
    @type fecha_fin : models.DateField(null=True)

    @param costo_temporal: es el tiempo estimativo que llevara realizar esa fase
    @type costo_temporal : models.PositiveIntegerField(default=0, null=True)

    @param costo_monetario : son los recursos monetarios estimativos a utilizarse para realizar esa fase
    @type costo_monetario : models.PositiveIntegerField(null=True)

    @param predecesor : corresponde a la fase que antecede a esta fase
    @type predecesor : models.ForeignKey('self', related_name='fase_predecesor', null=True, blank=True, default=None)

    @param sucesor : corresponde a la fase que viene a continuacion a esta fase y esta relacionada con la misma
    @type sucesor : models.ForeignKey('self', related_name='fase_sucesor', null=True, blank=True, default=None)

    @param roles : son los roles existentes en esa fase
    @type roles : models.ManyToManyField(Rol, related_name='roles_de_fase')
    """

    ESTADOS = (
        ('Abierta', 'abierta'),  #estos son estados de prueba
        ('Cerrada', 'cerrada'),
    )
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=7,
                              choices=ESTADOS,
                              default='Abierta')
    proyecto = models.ForeignKey(Proyecto, related_name='proyecto')
    fecha_ini = models.DateField(default=date.today, null=True)
    fecha_fin = models.DateField(default=date.today, null=True)
    costo_temporal = models.PositiveIntegerField(default=0, null=True)
    costo_monetario = models.PositiveIntegerField(default=0, null=True)
    orden = models.PositiveIntegerField(auto_created=True, default=0)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_fase', kwargs={'pk': self.pk})

