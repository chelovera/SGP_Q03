"""  Solo agregamos los campos que no se especifican en User del admin que trae por defecto DJango.
    EL ADMIN de Django guarda los siguientes campos:

    username Nombre de Usuario;
    password;
    email;
    first name y por ultimo,
    surname.

    De estos campos utilizaremos username, password, email y agregaremos las que faltan

"""
from django.db import models
from django.contrib.auth.models import User



class Roles(models.Model):
    nombre= models.CharField(max_length=30, unique=True)
    crear_usuario= models.BooleanField(default=False)           # - Permisos de Administracion de usuarios
    modificar_usuario= models.BooleanField(default=False)
    eliminar_usuario= models.BooleanField(default=False)

    crear_rol= models.BooleanField(default=False)               # - Permisos de Administracion de roles
    modificar_rol= models.BooleanField(default=False)
    eliminar_rol= models.BooleanField(default=False)

    crear_proyecto= models.BooleanField(default=False)          # - Permisos de Administracion de Proyectos
    iniciar_proyecto= models.BooleanField(default=False)
    finalizar_proyecto= models.BooleanField(default=False)
    eliminar_proyecto= models.BooleanField(default=False)

    crear_fase= models.BooleanField(default=False)              # - Permisos de Administracion de fases
    modificar_fase= models.BooleanField(default=False)
    cerrar_fase= models.BooleanField(default=False)

    asignar_miembro= models.BooleanField(default=False)         # - Permisos de administracion de los miembros del comite (incluye tareas del comite)
    modificar_miembros_comite=models.BooleanField(default=False)
    votar= models.BooleanField(default=False)
    consultar_solicitud= models.BooleanField(default=False)


    crear_item= models.BooleanField(default=False)              # - Permisos de Administracion de  Items
    eliminar_item= models.BooleanField(default=False)
    modificar_item= models.BooleanField(default=False)
    consultar_items= models.BooleanField(default=False)
    establecer_relacion= models.BooleanField(default=False)
    eliminar_relacion= models.BooleanField(default=False)
    aprobar_item= models.BooleanField(default=False)
    revivir_item= models.BooleanField(default=False)
    revertir_item= models.BooleanField(default=False)
    consultar_relaciones= models.BooleanField(default=False)


    crear_tipodeitem= models.BooleanField(default=False)        # - Permisos de Administracion de tipos de item
    modificar_tipodeitem= models.BooleanField(default=False)
    redefinir_tipodeotem= models.BooleanField(default=False)

    agregar_atributo= models.BooleanField(default=False)        # - Permisos de Administracion de atributos
    eliminar_atributo= models.BooleanField(default=False)
    consultar_atributos= models.BooleanField(default=False)


    crear_lineabase= models.BooleanField(default=False)         # - Permisos de Administracion de Lineas Base
    def __unicode__(self):
        return self.nombre



class UserProfile(models.Model):
   
    # Se enlaza UserProfile a una instancia de User model
    user = models.OneToOneField(User)

    # Agregamos los siguientes atributos
    website = models.URLField(blank=True)
    cedula = models.PositiveIntegerField(max_length=10, null=False, default=0)
    estado= models.BooleanField(default=True)       # Activo (True) o inactivo
    permiso= models.ManyToManyField(Roles)                      #El rol asociado al usuario
  #  picture = models.ImageField(upload_to='profile_images', blank=True)

    #para devolver algo significativo!
    def __unicode__(self):
        return self.user.username


