# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

from usuarios.models import Usuario
from fases.models import Fase
from .models import Rol, RolAsignar
#from proyectos.models import Proyecto


""" roles/views
Se controla lo que va a ser enviado al template para ser mostrado"""
class RolForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.history.back()'))

    class Meta:
        model = Rol
        exclude = ("fase", "usuario",)
""" Funcion rol_asignar lista todos los usuarios para que se pueda realizar la asignacion de roles a estos"""

@login_required
def rol_asignar(request, pk, template_name='roles/roles_asignar.html'):
    """
    @param pk
    @value es el primary key de la fase

    """
    usuarios = Usuario.objects.all().order_by('codigo')       # traigo a todos los usuarios para poder asignarles el rol elegido
    #rolesasignados=RolAsignar.objects.filter(pk=pk)
    rolesasignados = RolAsignar.objects.filter(pk=pk)
    lista_rolesasignados=[]
    for rol in rolesasignados:
        lista_rolesasignados.append(rol.usuario)        # guardamos los usuarios con el rol numero pk que recibimos (el que queremos asignar)
    lista_no_miembros = []
    for usuario in usuarios:
        if not usuario in lista_rolesasignados:
            lista_no_miembros.append(usuario)
    print(rolesasignados)
    print(lista_rolesasignados)
    print(lista_no_miembros)
    data = {}
    data['object_list'] = lista_no_miembros
    fase = Fase.objects.all()
    data['fase'] = fase
    rol = Rol.objects.get(pk=pk)
    data['rol'] = rol
    return render(request, template_name, data)


""" Funcion rol_asignar_usuario_create asignamos los roles a los usuarios elegidos
    @param pk
    @value es el primary key de rol
    @param codigo
    @value primary key de usuario """
@login_required
def rol_asignar_usuario_create(request, pk, codigo, template_name='roles/asignacion_correcta.html'):

    cod_usuario = request.user.id       #  id del usuario que esta tratando de asignar rol
    rol_actual = Rol.objects.get(pk=pk)
    fase_actual = rol_actual.fase
    proyecto = fase_actual.proyecto
    es_lider = proyecto.lider.codigo+1          #porque el usuario admin no se lista en la tabla user_user
    print(es_lider)
    if cod_usuario == es_lider:  #si el usuario es administrador entonces tiene que poder asignar rol
        usuario = Usuario.objects.get(codigo=codigo)
        r = RolAsignar(usuario=usuario, rol=rol_actual, confirmar=True)      #guardamos en la tabla RolAsignar el numero de usuario y el rol elegido
        r.save()# aca guardar que es miembro
        data={}
        data['rol']=rol_actual
        return render(request, template_name, data)
    else:
        data={}
        data['rol']=rol_actual
        return render(request, 'roles/rol_list_sin_permisos.html', data)


""" Funcion rol_list simplemente se listan los roles correspondientes a la fase que se esta procesando
    @param pk
    @value es el primary key de la fase
 """

@login_required
def rol_list(request, pk, template_name='roles/rol_list.html'):

    roles = Rol.objects.filter(fase=pk)
    data = {}
    data['object_list'] = roles
    fase = Fase.objects.get(pk=pk)
    data['fase'] = fase
    return render(request, template_name, data)

""" Funcion rol_create sirve para la creacion de un rol, dentro de la fase del proyecto
    @param pk
    @value es el primary key de la fase
 """
@login_required
def rol_create(request, pk, template_name='roles/rol_form.html'):

    cod_usuario = request.user.id
    proyecto_actual=Fase.objects.get(pk=pk).proyecto
    es_lider=proyecto_actual.lider.codigo+1
    if cod_usuario == es_lider:
        request.POST = request.POST.copy()
        request.POST.__setitem__('fase', pk)
        fase = Fase.objects.get(pk=pk)
        form = RolForm(request.POST or None)
        if form.is_valid():
            f = Rol(nombre=request.POST['nombre'], fase=fase,)
            f.save()
            return redirect('/proyectos/fases/roles/'+str(fase.codigo))
        return render(request, template_name, {'form': form})
    else:
        data = {}
        fase = Fase.objects.get(pk=pk)
        data['fase'] = fase
        return render(request, 'roles/rol_sin_permisos_create.html', data)


""" Funcion rol_update sirve para la editar algunos campos en los roles
    @param pk
    @value es el codigo del rol
 """

@login_required
def rol_update(request, pk, template_name='roles/rol_form.html'):

    rol = get_object_or_404(Rol, pk=pk)
    form = RolForm(request.POST or None, instance=rol)
    if form.is_valid():
        form.save()
        fase = Rol.objects.get(pk=pk).fase.codigo
        return redirect('/proyectos/fases/roles/'+str(fase))         #redirect a listarRoles
    return render(request, template_name, {'form': form})

""" Funcion rol_delete sirve para la editar algunos campos en los roles
    @param pk
    @value es el codigo del rol  a eliminar
 """


@login_required
def rol_delete(request, pk, template_name='roles/rol_confirm_delete.html'):
    server = get_object_or_404(Rol, pk=pk)

    if request.method == 'POST':
        fase = Rol.objects.get(pk=pk).fase.codigo  #quitamos el codigo de la fase
        server.delete()
        return redirect('/proyectos/fases/roles/'+str(fase))  #redirect a listarRoles
    return render(request, template_name, {'object': server})



