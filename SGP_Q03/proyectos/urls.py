# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""

from django.conf.urls import patterns, url
from .views import proyecto_create, proyecto_delete, proyecto_list, proyecto_update
from usuarios.views import configurar_comite
""" proyectos/urls
Se establecen los urls asociados al proyecto
"""
urlpatterns = patterns('',
  url(r'^$', proyecto_list, name='lista_proyecto'),
  url(r'^nuevo$', proyecto_create, name='nuevo_proyecto'),
  url(r'^editar/(?P<pk>\d+)$', proyecto_update, name='editar_proyecto'),
  url(r'^borrar/(?P<pk>\d+)$', proyecto_delete, name='borrar_proyecto'),
  url(r'^comite$',configurar_comite, name='configurar_comite')
)

