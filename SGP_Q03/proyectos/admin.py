# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""
from django.contrib import admin
from proyectos.models import Proyecto
"""
 Proyectos
"""
admin.site.register(Proyecto)