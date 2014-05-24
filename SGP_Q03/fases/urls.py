# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""

from django.conf.urls import patterns, url
from .views import fase_create, fase_delete, fase_list, fase_update, fase_search, fase_finalizar


""" fases/urls
Se establecen los urls asociados a fases
"""

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$', fase_list, name='lista_fase'),
                       url(r'^nuevo/(?P<pk>\d+)$', fase_create, name='nuevo_fase'),
                       url(r'^editar/(?P<pk>\d+)$', fase_update, name='editar_fase'),
                       url(r'^borrar/(?P<pk>\d+)$', fase_delete, name='borrar_fase'),
                       url(r'^search/(?P<pk>\d+)$', fase_search, name='buscar_fase'),
                       url(r'^finalizar/(?P<pk>\d+)$', fase_finalizar, name='fin_fase'),

)
