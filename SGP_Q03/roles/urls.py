# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""
from django.conf.urls import patterns, url
from .views import rol_create, rol_update, rol_list, rol_delete
""" ROLES/urls
Se establecen los distintos url que le pertenecen al modulo roles
"""
urlpatterns = patterns('',
  url(r'^$', rol_list, name='lista_rol'),
  url(r'^nuevo$', rol_create, name='nuevo_rol'),
  url(r'^editar/(?P<pk>\d+)$', rol_update, name='editar_rol'),
  url(r'^borrar/(?P<pk>\d+)$', rol_delete, name='borrar_rol')
)
