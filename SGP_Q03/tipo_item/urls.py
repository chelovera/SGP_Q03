__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import tipo_create, tipo_list, atributo_list, atributo_create, tipo_delete, atributo_delete, tipo_update, item_create, item_list, subir_archivos


""" fases/urls
Se establecen los urls asociados a fases
"""

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$', tipo_list, name='lista_tipo'),
                       url(r'^nuevo/(?P<pk>\d+)$', tipo_create, name='nuevo_tipo'),
                       url(r'^atributos/(?P<pk>\d+)$', atributo_list, name='lista_atributo'),
                       url('^atributos/nuevo/(?P<pk>\d+)$', atributo_create, name='nuevo_atributo'),
                       url(r'^borrar/(?P<pk>\d+)$', tipo_delete, name='borrar_tipo'),
                       url('^atributos/borrar/(?P<pk>\d+)$', atributo_delete, name='borrar_atributo'),
                       url(r'^editar/(?P<pk>\d+)$', tipo_update, name='editar_tipo'),
                       url(r'^items/(?P<pk>\d+)$', item_list, name='lista_item'),
                       url(r'^items/nuevo/(?P<pk>\d+)$', item_create, name='nuevo_item'),
                       url(r'^items/archivos/(?P<pk>\d+)$',subir_archivos, name='subir_archivos')


)
