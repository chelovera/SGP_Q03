# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""
from django.test import TestCase

from guardian.conf import settings
from guardian.compat import get_user_model
from guardian.management import create_anonymous_user
""" ROLES/TEST """

User = get_user_model()


class CustomUserTests(TestCase):
    def test_crear_usuario_anonimo(self):
        create_anonymous_user(object())
        self.assertEqual(1, User.objects.all().count())
        anonimo = User.objects.all()[0]
        self.assertEqual(anonimo.pk, settings.ANONYMOUS_USER_ID)