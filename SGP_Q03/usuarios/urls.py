# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""
from django.core.urlresolvers import reverse
from django.conf.urls import patterns, url
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from .views import usuario_list, usuario_create, usuario_delete, usuario_update, search
from .models import Usuario

""" usuarios/urls
Se establecen las distintas urls que se manejan desde usuarios
"""
urlpatterns = patterns('',
                       url(r'^$', usuario_list, name='lista_usuario'),
                       url(r'^nuevo$', usuario_create, name='nuevo_usuario'),
                       url(r'^create_user/$', (
                       CreateView.as_view(model=Usuario, get_success_url=lambda: reverse('usuarios/'),
                                          form_class=UserCreationForm, template_name="usuarios/usuario_form.html")),
                           name='create_user'),
                       url(r'^editar/(?P<pk>\d+)$', usuario_update, name='editar_usuario'),
                       url(r'^borrar/(?P<pk>\d+)$', usuario_delete, name='borrar_usuario'),
                       url(r'^search/$', search),
)

