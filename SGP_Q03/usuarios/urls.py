__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import UsuarioLista,UsuarioCrear,UsuarioBorrar,UsuarioModificar

urlpatterns = patterns('',
  url(r'^$', UsuarioLista.as_view(), name='lista_usuarios'),
  url(r'^nuevo$', UsuarioCrear.as_view(), name='nuevo_usuario'),
  url(r'^editar/(?P<pk>\d+)$', UsuarioModificar.as_view(), name='editar_usuario'),
  url(r'^borrar/(?P<pk>\d+)$', UsuarioBorrar.as_view(), name='borrar_usuario'),
)


