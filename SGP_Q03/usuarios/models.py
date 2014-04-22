from django.db import models
from django.core.urlresolvers import reverse
#from proyectos.models import Proyecto

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    telefono = models.PositiveIntegerField(default=0)
    cedula = models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=20, null=False)
    direccion = models.CharField(max_length=50, null=False)
    estado = models.BooleanField(default=True)
    #proyectos = models.ManyToManyField(Proyecto, related_name='ProyectoBase')

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_usuario', kwargs={'pk': self.pk})


