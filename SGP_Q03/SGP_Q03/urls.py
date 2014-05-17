# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""

from django.conf.urls import patterns, include, url

from django.contrib import admin

""" SGP_P03/urls
Se establecen los urls asociados de cada modulo del proyecto
"""

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'SGP_Q03.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('login.urls')),
                       url(r'^usuarios/', include('usuarios.urls')),
                       url(r'^proyectos/', include('proyectos.urls')),
                       url(r'^proyectos/fases/', include('fases.urls')),
                       url(r'^proyectos/fases/roles/', include('roles.urls')),
                       url(r'^proyectos/fases/tipo_item/', include('tipo_item.urls')),
                       #url(r'^proyectos/fases/comite/', include('comite.urls')),
)
