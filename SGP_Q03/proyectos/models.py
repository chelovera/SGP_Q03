# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""
from datetime import date

from django.db import models
from django.core.urlresolvers import reverse
from usuarios.models import Usuario


"""
Django proyectos/models

"""

class Proyecto(models.Model):

    """
    Estos son los campos que contiene proyectos/models.py

    @param codigo: Es el primary key, se genera automaticamente
    @type codigo: models.AutoField(primary_key= True)

    @param nombre: Es el nombre del proyecto
    @type nombre: models.CharField(max_length=50)

    @param descripcion: en este campo se indican las caracteristicas mas resaltantes del proyecto
    @type descripcion : models.CharField(max_length=200)

    @param estado: indica que el proyecto puede estar en estado Pendiente o Finalizado
    @type estado: models.CharField(max_length=10, choices=ESTADOS, default='Pendiente')

    @param fecha_ini: es la fecha de inicio del proyecto
    @type fecha_ini: models.DateField(null=True)

    @param fecha_fin:  es la fecha de finalizacion del proyecto
    @type fecha_fin : models.DateField(null=True)

    @param costo_temporal: es el tiempo estimativo que llevara realizar el proyecto
    @type costo_temporal : models.PositiveIntegerField(default=0, null=True)

    @param costo_monetario : son los recursos monetarios estimativos a utilizarse para realizar el proyecto
    @type costo_monetario : models.PositiveIntegerField(null=True)

    @param lider : se establece el lider del proyecto
    @type lider : models.ForeignKey(Usuario)
    """



    #estos son estados de prueba
    ESTADOS = (
        ('Pendiente', 'pendiente'),
        ('Iniciado', 'iniciado'),
        ('Finalizado', 'finalizado'),
    )
    codigo= models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=10,
                              choices=ESTADOS,
                              default='Pendiente')
    fecha_ini=models.DateField(null=True,default = date.today)
    fecha_fin=models.DateField(null=True, default = date.today)
    costo_temporal= models.PositiveIntegerField(default=0, null=True)
    costo_monetario= models.PositiveIntegerField(default=0, null=True) # solo enteros positivos nada mas
    lider = models.ForeignKey(Usuario, related_name='lider')
    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_proyecto', kwargs={'pk': self.pk})

    class Meta:
        ordering=('codigo',)
