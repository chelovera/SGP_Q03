__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import fase_create, fase_delete, fase_list, fase_update

urlpatterns = patterns('',
  url(r'^$', fase_list, name='lista_fase'),
  url(r'fases/^nuevo$', fase_create, name='nuevo_fase'),
  url(r'fases/^editar/(?P<pk>\d+)$', fase_update, name='editar_fase'),
  url(r'fases/^borrar/(?P<pk>\d+)$', fase_delete, name='borrar_fase'),
)
