# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       # existing patterns here...
                       url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login/index.html'},
                           name='login', ),
                       url(r'logout/', 'django.contrib.auth.views.logout_then_login', name='logout', ),
)
