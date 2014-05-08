__author__ = 'alfaro'

from django.conf.urls import patterns, url
from .views import tipo_create


""" fases/urls
Se establecen los urls asociados a fases
"""

urlpatterns = patterns('',
  url(r'^nuevo$', tipo_create, name='nuevo_tipo'),

)
