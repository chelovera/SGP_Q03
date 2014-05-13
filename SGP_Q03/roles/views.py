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
from fases.models import Fase
from .models import Rol
#from proyectos.models import Proyecto
#from usarios.models import Usuario

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
        fields = (
            "nombre",
            #"fase",
            #"usuario",
            "crear_tipo_item",
            "editar_tipo_item",
            "eliminar_tipo_item",
            "crear_linea_base",
            "abrir_linea_base",
            "crear_item",
            "editar_item",
            "eliminar_item",
            "aprobar",
            "revivir",
            "reversionar",
            "asignar_padre",
            "asignar_antecesor",
        )


"""

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
        model = Rol
        fields = (
            #"nombre",
            #"fase",
            "usuario",
            "crear_tipo_item",
            "editar_tipo_item",
            "eliminar_tipo_item",
            "crear_linea_base",
            "abrir_linea_base",
            "crear_item",
            "editar_item",
            "eliminar_item",
            "aprobar",
            "revivir",
            "reversionar",
            "asignar_padre",
            "asignar_antecesor",
        )

@login_required
def asignar_rol(request, pk, template_name='roles/asignar_rol'):
    data = {}
    fase = Fase.objects.get(pk=pk)
    data['fase'] = fase
    request.POST = request.POST.copy()
    request.POST.__setitem__('fase', pk)
    fase = Fase.objects.get(pk=pk)
    form = RolFormAsignar(request.POST or None)
    if form.is_valid():
        f = Rol(fase=fase,)
        f.save()
        return redirect('lista_proyecto')               # si necesitamos pasar a la direccion 'lista_rol' necesito pasar un parametro y eso no se como hacer....creo que tiene algo que ver con crispy osea enviar el pk con el boton guardar en form
    return render(request, template_name, {'form': form})

"""
@login_required
def rol_list(request, pk, template_name='roles/rol_list.html'):
    roles = Rol.objects.filter(fase=pk)
    data = {}
    data['object_list'] = roles
    fase = Fase.objects.get(pk=pk)
    data['fase'] = fase
    return render(request, template_name, data)


""" @login_required
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


""" @login_required
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
        return redirect('lista_proyecto')
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
