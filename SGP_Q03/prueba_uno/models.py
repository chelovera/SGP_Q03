from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
   
    # Se enlaza UserProfile a una instancia de User model
    user = models.OneToOneField(User)

    # Agregamos los siguientes atributos
    website = models.URLField(blank=True)
    cedula = models.PositiveIntegerField(max_length=10, null=False, default=0)
  #  picture = models.ImageField(upload_to='profile_images', blank=True)

    #para devolver algo significativo!
    def __unicode__(self):
        return self.user.username

