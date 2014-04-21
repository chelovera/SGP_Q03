__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import index

urlpatterns = patterns('',
                       url(r'^$', index, name='proyectos')
)