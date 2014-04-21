from django.db import models
from django.contrib.auth.models import User


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
    lider = models.ForeignKey(User)

    class Meta:
        permissions = (
            ('ver_proyecto', 'Ver proyecto'),
        )

    class Meta:
        permissions = (
            ('crear_proyecto', 'Crear proyecto'),
            ('ver_proyecto', 'Ver proyecto'),
            ('modificar_proyecto', 'Modificar proyecto'),
            ('eliminar_proyecto', 'Eliminar proyecto'),
        )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.nombre

