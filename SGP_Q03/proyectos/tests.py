# -*- coding: ISO-8859-1
""" Sistema de Gesti�n de Proyectos SGP
Grupo Q03
Ingenier�a de Software II
@author: Mabel Pe�a - Alvaro Rodr�guez
A�o: 2014
"""
from django.test import TestCase
from usuarios.models import Usuario
from .models import Proyecto

class TestProyectoView(TestCase):

    def crear_usuario(self,username, nombre= 'test', apellido='test', cedula='12345', email='test@test.com',password= 'test'):
        return Usuario.objects.create(username= username,nombre= nombre, apellido=apellido, cedula=cedula, email=email,password= password)

    def crear_proyecto(self, nombre):
        w = self.crear_usuario(username= 'liderU')
        P = Proyecto.objects.create(nombre = nombre, descripcion = 'Esto es una prueba', lider=w)
        return (P)

    def test_crear_proyecto(self):
        u = self.crear_proyecto(nombre ='test')
        self.assertTrue(isinstance(u , Proyecto))
        self.assertEqual(u.__unicode__(), u.nombre)
        print('ejecutando test crear proyecto')
