__author__ = 'penhagonzalez'

from django.conf.urls import patterns, url
from .views import comite_create

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)$', comite_create, name='nuevo_comite'),


)


