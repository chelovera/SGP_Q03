# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""
from django.contrib import admin
from proyectos.models import Proyecto
"""
 Proyectos
"""
admin.site.register(Proyecto)