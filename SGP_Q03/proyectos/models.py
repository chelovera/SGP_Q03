from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Proyecto(models.Model):
    #estos son estados de prueba
    ESTADOS = (
        ('P', 'pendiente'),
        ('F', 'finalizado'),
    )
    codigo= models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    numero_fase=models.PositiveIntegerField(default=1)
    #usuarios= models.ManyToManyField(Usuario, related_name='UsuarioBase')
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=1,
                              choices=ESTADOS,
                              default='P')
    #lider = models.ForeignKey(Usuario)
    fecha_ini=models.DateTimeField(null=True)
    fecha_fin=models.DateTimeField(null=True)
    costo_temporal= models.PositiveIntegerField(default=0, null=True)
    costo_monetario= models.PositiveIntegerField(null=True) # solo enteros positivos nada mas

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editar_proyecto', kwargs={'pk': self.pk})