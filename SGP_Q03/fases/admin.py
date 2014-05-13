# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014

"""
from django.contrib import admin
from fases.models import Fase
"""
 Proyectos
"""
admin.site.register(Fase)
