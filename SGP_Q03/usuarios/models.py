from django.db import models

class Usuario(models.Model):
    username = models.CharField()
    password = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    telefono = models.PositiveIntegerField(default=0)
    cedula = models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=20, null=False)
    direccion = models.CharField(max_length=50, null=False)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre

