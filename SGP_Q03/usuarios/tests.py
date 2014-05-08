# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""



from django.test import TestCase
from .models import Usuario
from django.core.urlresolvers import reverse

class TestUsuarioView(TestCase):

    def crear_usuario(self, username='test',nombre= 'test', apellido='test', cedula='12345', email='test@test.com',password='test', is_superuser=False):
        return Usuario.objects.create(username=username ,nombre= nombre, apellido=apellido, cedula=cedula, email=email,password= password, is_superuser=is_superuser)


    def test_crear_usuario(self):
        u = self.crear_usuario()
        self.assertTrue(isinstance(u,Usuario))
        self.assertEqual(u.__unicode__(), u.nombre)
        print('ejecutando test crear usuario')

    def test_crear_superusuario(self):
        u = Usuario.objects.create_superuser('test','test@gmail.com','test')
        self.assertTrue(isinstance(u,Usuario))
        self.assertTrue(u.is_superuser,True)
        self.assertEqual(u.__unicode__(), u.nombre)
        print('ejecutando test crear superusuario')