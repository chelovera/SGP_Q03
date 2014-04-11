from django.db import models

'''Prueba de documentacion



'''
# Create your models here.
class Proyecto(models.Model):
    #estos son estados de prueba
    ESTADOS = (
        ('A', 'abierto'),
        ('C', 'cerrado'),
        ('R', 'revision'),
    )
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=1,
                              choices=ESTADOS,
                              default='A')
    #    idLider
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.nombre

