from django.db import models
from django.core.urlresolvers import reverse
from usuarios.models import Usuario


class Proyecto(models.Model):
    #estos son estados de prueba
    ESTADOS = (
        ('Pendiente', 'pendiente'),
        ('Finalizado', 'finalizado'),
    )
    codigo= models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=10,
                              choices=ESTADOS,
                              default='Pendiente')
    fecha_ini=models.DateField(null=True)
    fecha_fin=models.DateField(null=True)
    costo_temporal= models.PositiveIntegerField(default=0, null=True)
    costo_monetario= models.PositiveIntegerField(default=0, null=True) # solo enteros positivos nada mas
    lider = models.ForeignKey(Usuario)
    miembros = models.ManyToManyField(Usuario, related_name='miembros_proyecto')
    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_proyecto', kwargs={'pk': self.pk})

    class Meta:
        ordering=('codigo',)
