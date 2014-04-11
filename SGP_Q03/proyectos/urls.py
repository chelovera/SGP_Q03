__author__ = 'alfaro'

from django.conf.urls import patterns, url
from proyectos import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index')
)