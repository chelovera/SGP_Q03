from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Rol(models.Model):

    nombre= models.CharField(max_length=25)
    crear_tipo_item = models.BooleanField()
    editar_tipo_item = models.BooleanField()
    eliminar_tipo_item = models.BooleanField()
    crear_linea_base= models.BooleanField()
    abrir_linea_base= models.BooleanField()
    crear_item=models.BooleanField()
    editar_item=models.BooleanField()
    eliminar_item=models.BooleanField()
    aprobar=models.BooleanField()
    revivir=models.BooleanField()
    reversionar=models.BooleanField()
    asignar_padre=models.BooleanField()
    asignar_antecesor=models.BooleanField()
    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_rol', kwargs={'pk': self.pk})