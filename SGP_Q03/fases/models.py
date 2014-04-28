from django.core.urlresolvers import reverse
from django.db import models
from proyectos.models import Proyecto




class Fase(models.Model):
    #estos son estados de prueba
    ESTADOS = (
        ('Abierta', 'abierta'),
        ('Cerrada', 'cerrada'),
    )
    codigo= models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=7,
                              choices=ESTADOS,
                              default='Abierta')
    proyecto = models.ForeignKey(Proyecto)
    #tipos_de_items = models.ForeignKey(TipoItem)
    #items= models.ForeignKey(Item)
    fecha_ini=models.DateField(null=True)
    fecha_fin=models.DateField(null=True)
    costo_temporal= models.PositiveIntegerField(default=0, null=True)
    costo_monetario= models.PositiveIntegerField(null=True)
    #lineas_base=models.ForeignKey(LineaBase)
    predecesor=models.ForeignKey('self', related_name='fase_predecesor')
    sucesor=models.ForeignKey('self', related_name='fase_sucesor')
    #fases= models.('self', related_name='')


    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_fase', kwargs={'pk': self.pk})