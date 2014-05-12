from django.db import models
from fases.models import Fase
import eav
# Create your models here.


class Tipo_Item(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    fase = models.ForeignKey(Fase, related_name='fase_tipo_item')

    def __unicode__(self):
        return self.nombre




class Atributo(models.Model):
    TIPOS = (
        ('Numerico', 'numerico'),  #estos son estados de prueba
        ('Logico', 'logico'),
        ('Cadena', 'cadena'),
        ('Fecha', 'fecha'),
    )
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=8,
                            choices=TIPOS,
                            default='Numerico')
    tipo_item = models.ForeignKey(Tipo_Item)

    def __unicode__(self):
        return self.nombre