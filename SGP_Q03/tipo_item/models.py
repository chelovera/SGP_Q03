from django.db import models
from fases.models import Fase

# Create your models here.


class Tipo_Item(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    fase = models.ForeignKey(Fase, related_name='fase_tipo_item')
    def __unicode__(self):
        return self.nombre


class Item(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    costo = models.PositiveIntegerField(default=1)
    dificultad = models.PositiveIntegerField(default=1)
    tipo_item = models.ForeignKey(Tipo_Item, related_name='tipo_item')
    fase= models.ForeignKey(Fase, related_name='fase_item')
    actual = models.BooleanField(default=True)

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
    valor = models.CharField(max_length=100, null=True, blank=True)
    tipo_item = models.ForeignKey(Tipo_Item, related_name='tipo_item_atributo')
    item= models.ForeignKey(Item, related_name='item', null=True, blank=True, default=None)
    def __unicode__(self):
        return self.nombre
