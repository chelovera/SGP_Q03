
# Create your tests here.
"""Prueba de Autenticacion

    Este test devuelve OK en el caso que no ocurran errores,
    En caso contrario devuelve una descripcion del error ocurrido, seguido de la linea y la clase
    en la que ocurrio el error"""

from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestLogin(TestCase):
    """
    TestLogin
        Se define un persona para iniciar nuestro test
        Completamos los campos requeridos con los siguientes valores:
        username: prueba
        email: test@test.com
        password: prueba
    """

    def setUp(self):
        self.client = Client()
        self.username = 'prueba'
        self.email = 'test@test.com'
        self.password = 'prueba'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)

    """ test_login_exitoso
        Con el usuario creado (username y password correctos) probamos si se loguea correctamente
    """

    def test_login_exitoso(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True, 'el sistema de login no esta funcionando correctamente')
        print('ejecutando test 1 login exitoso')
    """ test_usuario_incorrecto
        Se prueba un usuario incorrecto con el password del usuario 'prueba' creado recientemente
    """

    def test_usuario_incorrecto(self):
        login = self.client.login(username='ola que ase', password=self.password)
        self.assertEqual(login, False, 'un usuario incorrecto realizo un login')
        print('ejecutando test 2 usuario incorrecto')
    """ test_password_incorrecto
        Se prueba un usuario correcto con el password incorrecto
    """


    def test_password_incorrecto(self):
        login = self.client.login(username=self.username, password='ola que ase password')
        self.assertEqual(login, False, 'un password incorrecto realizo un login')
        print('ejecutando test 3 password incorrecto')
    """ test_usuario_vacio
        Se prueba un usuario vacio con el password del usuario 'prueba' creado recientemente
    """


    def test_usuario_vacio(self):
        login = self.client.login(username='', password=self.password)
        self.assertEqual(login, False, 'un usuario vacio realizo un login')
        print('ejecutando test 4 usuario vacio')
    """ test_password_vacio
        Probamos con el usuario correcto con el password vacio
    """


    def test_password_vacio(self):
        login = self.client.login(username=self.username, password='')
        self.assertEqual(login, False, 'un password vacio realizo un login')
        print('ejecutando test 5 password vacio')