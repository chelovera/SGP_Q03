from django.db import models
from fases.models import Fase
# Create your models here.

class Tipo_Item(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    fase=models.ForeignKey(Fase,related_name='fase_tipo_item')

class Atributos(models.Model):
    TIPOS = (
        ('Fecha',models.DateTimeField()),#estos son estados de prueba
        ('Email', models.EmailField()),
        ('Numerico', models.IntegerField()),
        ('Boolean', models.BooleanField()),
    )
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10,
                              choices=TIPOS,
                              default='Fecha')

