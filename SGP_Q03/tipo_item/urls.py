__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import tipo_create, tipo_list, atributo_list, atributo_create


""" fases/urls
Se establecen los urls asociados a fases
"""

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$', tipo_list, name='lista_tipo'),
                       url(r'^nuevo/(?P<pk>\d+)$', tipo_create, name='nuevo_tipo'),
                       url(r'^atributos/(?P<pk>\d+)$', atributo_list, name='lista_atributo'),
                       url('^atributos/nuevo/(?P<pk>\d+)$', atributo_create, name='nuevo_atributo')
        )
