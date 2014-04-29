__author__ = 'alfaro'
from django.conf.urls import patterns, url
from .views import rol_create, rol_update, rol_list

urlpatterns = patterns('',
  url(r'^(?P<pk>\d+)$', rol_list, name='lista_rol'),
  url(r'^nuevo$', rol_create, name='nuevo_rol'),
  url(r'^editar/(?P<pk>\d+)$', rol_update, name='editar_rol'),
)
