__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import usuario_list,usuario_create,usuario_delete,usuario_update

urlpatterns = patterns('',
  url(r'^$', usuario_list, name='lista_usuario'),
  url(r'^nuevo$', usuario_create, name='nuevo_usuario'),
  url(r'^editar/(?P<pk>\d+)$', usuario_update, name='editar_usuario'),
  url(r'^borrar/(?P<pk>\d+)$', usuario_delete, name='borrar_usuario'),
)

