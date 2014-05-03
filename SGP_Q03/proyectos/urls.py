# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""

from django.conf.urls import patterns, url
from .views import proyecto_create, proyecto_delete, proyecto_list, proyecto_update

""" proyectos/urls
Se establecen los urls asociados al proyecto
"""
urlpatterns = patterns('',
  url(r'^$', proyecto_list, name='lista_proyecto'),
  url(r'^nuevo$', proyecto_create, name='nuevo_proyecto'),
  url(r'^editar/(?P<pk>\d+)$', proyecto_update, name='editar_proyecto'),
  url(r'^borrar/(?P<pk>\d+)$', proyecto_delete, name='borrar_proyecto'),
)

