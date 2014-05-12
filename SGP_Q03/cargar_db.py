from usuarios.models import Usuario
from proyectos.models import Proyecto
from fases.models import Fase
from tipo_item.models import Tipo_Item
#Proyecto.objects.all().delete()
#ejecutar asi ./manage.py shell < cargar_db.py
Usuario.objects.all().delete()
Tipo_Item.objects.all().delete()
Fase.objects.all().delete()
Proyecto.objects.all().delete()

usuario1 = Usuario.objects.create_user(username='alvaro_user', nombre='Alvaro', apellido='Rodriguez',
                                       telefono='0961940704', cedula='4617510',
                                       direccion='Calle Rio Negro esq. Rio Jejui 315',
                                       email='alfa.alvaro.rodriguez@gmail.com', password='alvaro_user')
usuario2 = Usuario.objects.create_user(username='homero', nombre='Homero', apellido='Simpson', telefono='5556832',
                                       cedula='123467', direccion='Avenida Siempreviva 742',
                                       email='amantedelacomida53@aol.com', password='homero')
usuario3 = Usuario.objects.create_user(username='walter', nombre='Walter', apellido='White', telefono='5551234',
                                       cedula='8910111', direccion='308 de Negra Arroyo Lane', email='walter@gmail.com',
                                       password='walter')
usuario4 = Usuario.objects.create_user(username='john', nombre='John', apellido='Snow', telefono='5555678',
                                       cedula='2131415', direccion='en el muro', email='john@gmail.com',
                                       password='john')
usuario5 = Usuario.objects.create_user(username='bruce', nombre='Bruce', apellido='Banner', telefono='5559012',
                                       cedula='1617181', direccion='ni idea', email='banner@gmail.com',
                                       password='banner')

proyecto1 = Proyecto(nombre='alpha project', descripcion='este proyecto corresponde a Alvaro Rodriguez',
                     costo_temporal=10, costo_monetario=10, lider=usuario1)
proyecto2 = Proyecto(nombre='beta project', descripcion='este proyecto corresponde a Homero Simpson', costo_temporal=10,
                     costo_monetario=10, lider=usuario2)
proyecto3 = Proyecto(nombre='gamma project', descripcion='este proyecto corresponde a Walter White', costo_temporal=10,
                     costo_monetario=10, lider=usuario3)
proyecto4 = Proyecto(nombre='delta project', descripcion='este proyecto corresponde a John Snow', costo_temporal=10,
                     costo_monetario=10, lider=usuario4)
proyecto5 = Proyecto(nombre='epsilon project', descripcion='este proyecto corresponde a Bruce Banner',
                     costo_temporal=10, costo_monetario=10, lider=usuario5)

proyecto1.save()
proyecto2.save()
proyecto3.save()
proyecto4.save()
proyecto5.save()

fase1 = Fase(nombre='primera fase', descripcion='primera fase ', proyecto=proyecto1)
fase2 = Fase(nombre='segunda fase', descripcion='segunda fase', proyecto=proyecto1)
fase3 = Fase(nombre='tercera fase', descripcion='tercera fase', proyecto=proyecto1)
fase4 = Fase(nombre='cuarta fase', descripcion='cuarta fase', proyecto=proyecto1)
fase5 = Fase(nombre='quinta fase', descripcion='quinta fase', proyecto=proyecto1)

fase1.save()
fase2.save()
fase3.save()
fase4.save()
fase5.save()

tipo1= Tipo_Item(nombre='requerimiento funcional',descripcion='representa un requerimiento funcional para la fase',fase=fase1)
tipo2= Tipo_Item(nombre='requerimiento no funcional',descripcion='representa un requerimiento no funcional para la fase',fase=fase1)
tipo3= Tipo_Item(nombre='caso de uso',descripcion='representa casos de uso para la fase',fase=fase1)
tipo4= Tipo_Item(nombre='diagrama',descripcion='representa cualquier tipo de diagrama',fase=fase1)
tipo5= Tipo_Item(nombre='requerimiento de hardware',descripcion='representa una configuracion de hardware',fase=fase1)

tipo1.save()
tipo2.save()
tipo3.save()
tipo4.save()
tipo5.save()