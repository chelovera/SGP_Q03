# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       # existing patterns here...
                       url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login/index.html'},
                           name='login', ),
                       url(r'logout/', 'django.contrib.auth.views.logout_then_login', name='logout', ),
)
