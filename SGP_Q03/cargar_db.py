from usuarios.models import Usuario
from proyectos.models import Proyecto


#Proyecto.objects.all().delete()
Usuario.objects.all().delete()
u = Usuario.objects.create_user(username='alvarito',nombre='Alvaro',apellido='Rodriguez',telefono='0961940704',cedula='4617510',direccion='Calle Rio Negro esq. Rio Jejui nro 315', email='test@test.com',password='alvarito')
