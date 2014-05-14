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
from django.views.generic import TemplateView
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

class RolFormAsignar(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RolFormAsignar, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.history.back()'))

    class Meta:
        model = RolAsignar
        fields = (
            #"nombre",
            #"fase",
            "codigo",
            #"usuario",
            "confirmar",

        )

@login_required
def rol_asignar(request, pk, template_name='roles/roles_asignar.html'):
    """
    pk= es el primary key del rol
    """
    usuarios = Usuario.objects.all().order_by('codigo')       # traigo a todos los usuarios para poder asignarles el rol elegido
    data = {}
    data['object_list'] = usuarios
    fase = Fase.objects.all()
    data['fase'] = fase
    rol = Rol.objects.get(pk=pk)
    data['rol'] = rol
    #proyecto = fase.proyecto.nombre
    #data['proyecto'] = proyecto
    return render(request, template_name, data)  #falta setear usuario y rol



@login_required
def rol_asignar_usuario_create(request, pk, codigo, template_name='roles/rol_form.html'):
    """
     pk= primary key de rol
     codigo=primary key de usuario
    """
    rol = Rol.objects.get(pk=pk)
    usuario = Usuario.objects.get(codigo=codigo)
    form=RolFormAsignar(request.POST or None)
    if form.is_valid():
        asignar = RolAsignar(rol=rol, usuario=usuario, confirmar=request.POST['confirmar'])
        asignar.save()
        #return redirect('lista_proyecto')
        return redirect('/proyectos/fases/roles/asignar/'+str(pk))
    return render(request, template_name, {'form': form})


""" def atributo_create(request, pk, template_name='tipos/atributo_form.html'):
    tipo_item = Tipo_Item.objects.get(pk=pk)
    form = AtributoForm(request.POST or None)

    if form.is_valid():
        atributo = Atributo(nombre=request.POST['nombre'], tipo=request.POST['tipo'], tipo_item=tipo_item,)
        atributo.save()
        return redirect('/proyectos/fases/tipo_item/atributos/'+pk)
    return render(request, template_name, {'form': form})
"""



@login_required
def rol_list(request, pk, template_name='roles/rol_list.html'):
    """ pk= es el primary key de la fase
    """
    roles = Rol.objects.filter(fase=pk)
    data = {}
    data['object_list'] = roles
    fase = Fase.objects.get(pk=pk)
    data['fase'] = fase
    return render(request, template_name, data)


"""
@login_required
def fase_list(request, pk ,  template_name='fases/fase_list.html'):
    fases = Fase.objects.filter(proyecto=pk)
    data = {}
    data['object_list'] = fases
    #arreglo temporal
    #recuperamos el proyecto, ahi usamos el lider para que pueda ver las opciones de configurar fases y demas
    proyecto = Proyecto.objects.get(pk=pk)
    usuario = Usuario.objects.get(pk=proyecto.lider.pk)
    request_user= Usuario.objects.get(nombre=request.user.username)
    data['proyecto']=proyecto
    if request_user.pk == usuario.pk:
        return render(request, template_name, data)
    else:
        return render(request, 'fases/fase_list_sin_permisos.html', {}) """

@login_required
def rol_create(request, pk, template_name='roles/rol_form.html'):
    """pk= es el primary key del  """
    request.POST = request.POST.copy()
    request.POST.__setitem__('fase', pk)
    fase = Fase.objects.get(pk=pk)
    form = RolForm(request.POST or None)
    #proyecto = Proyecto.objects.get(pk=pk) #traigo de la BD el proyecto, para utilizar el campo 'lider'
    #usuario = Usuario.objects.get(pk=proyecto.lider.pk) # traigo los datos del lider del proyecto
    #request_user = Usuario.objects.get(nombre=request.user.username)  # traigo los datos del usuario actual
    #if request_user.pk == usuario.pk:                                   #comparo si el usuario actual es realmente el lider del proyecto
    if form.is_valid():
        f = Rol(nombre=request.POST['nombre'], fase=fase,)
        f.save()
        return redirect('/proyectos/fases/roles/'+str(fase.codigo))
    return render(request, template_name, {'form': form})
    #else:
     #   return render(request, 'roles/rol_list_sin_permisos.html', {})


"""
@login_required
def fase_create(request,pk, template_name='fases/fase_form.html'):

    request.POST=request.POST.copy()
    request.POST.__setitem__('proyecto',pk)
    proyecto=Proyecto.objects.get(pk=pk)
    form = FaseForm(request.POST or None)

    if form.is_valid():
        #form.save()
        f = Fase(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'],proyecto=proyecto,)
        f.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form':form})
"""

@login_required
def rol_update(request, pk, template_name='roles/rol_form.html'):
    rol = get_object_or_404(Rol, pk=pk)
    #fase = Fase.objects.get(pk=pk)
    form = RolForm(request.POST or None, instance=rol)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')           # falta redirigir a la parte de '/proyectos/fases/roles/'+str(....)
    return render(request, template_name, {'form': form})


""" @login_required
def fase_update(request, pk, template_name='fases/fase_form.html'):

    fase = get_object_or_404(Fase, pk=pk)
    form = FaseForm(request.POST or None, instance=fase)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form':form})"""

@login_required
def rol_delete(request, pk, template_name='roles/rol_confirm_delete.html'):
    server = get_object_or_404(Rol, pk=pk)
    #fase = Fase.objects.get(pk=pk)
    if request.method == 'POST':
        server.delete()
        return redirect('lista_proyecto')  # cambiar aca cuando sepa pasar el parametro necesario
    return render(request, template_name, {'object': server})


""" @login_required
def fase_delete(request, pk, template_name='fases/fase_confirm_delete.html'):
    server = get_object_or_404(Fase, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('lista_fase')
    return render(request, template_name, {'object': server})"""
