from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

class Usuario(User):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    telefono = models.PositiveIntegerField(default=0)
    cedula = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=50, null=False)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_usuario', kwargs={'pk': self.pk})


