__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import proyecto_create, proyecto_delete, proyecto_list, proyecto_update

urlpatterns = patterns('',
  url(r'^$', proyecto_list, name='lista_proyecto'),
  url(r'^nuevo$', proyecto_create, name='nuevo_proyecto'),
  url(r'^editar/(?P<pk>\d+)$', proyecto_update, name='editar_proyecto'),
  url(r'^borrar/(?P<pk>\d+)$', proyecto_delete, name='borrar_proyecto'),
)

