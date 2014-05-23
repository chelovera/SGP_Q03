# -*- coding: ISO-8859-1
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Hidden

from .models import Fase
from usuarios.models import Usuario
from proyectos.models import Proyecto
from roles.models import RolAsignar

class FaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FaseForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # para que no renderice el <form></form>
        #self.helper.form_tag = False
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.;'))

    def clean_proyecto(self):
        """
        @param self: se ejecuta sobre un formulario para asignarle un proyecto
        @return: se retorna el proyecto de la fase
        """
        proyecto = self.cleaned_data['proyecto']
        proyecto = Proyecto.objects.get(codigo=proyecto.codigo)
        return proyecto

    class Meta:
        model = Fase
        fields = (
            "nombre",
            "descripcion",
            "fecha_ini",
            "fecha_fin",
            "costo_temporal",
            "costo_monetario",
        )


@login_required
def es_miembro(usu, proyectito):
    """
     se devuelve true si es miembro del proyecto
    """
    todo_rol_asignar = RolAsignar.objects.filter(usuario=usu.id-1)
    lista_de_proyectos_del_usuario = []
    for rol_a in todo_rol_asignar:
        lista_de_proyectos_del_usuario.append(rol_a.proyecto)
    for verificar in lista_de_proyectos_del_usuario:
        if verificar.codigo == proyectito.codigo:         #entonces es miembro del proyecto
            return True
        return False


"""
@login_required
def fase_list(request, pk, template_name='fases/fase_list.html'):
    #pk= es el primary key del proyecto
    fases = Fase.objects.filter(proyecto=pk).order_by('codigo')
    data = {}
    data['object_list'] = fases
    #arreglo temporal
    #recuperamos el proyecto, ahi usamos el lider para que pueda ver las opciones de configurar fases y demas
    proyecto = Proyecto.objects.get(pk=pk)
    usuario_actual = request.user
    print "request-user"
    print usuario_actual
    #ver_miembro = miembro(usuario_actual, proyecto)

    usuario = Usuario.objects.get(pk=proyecto.lider.pk) #este es el usuario lider
    print "usuario-lider"
    print usuario
    request_user = Usuario.objects.get(username=request.user.username)
    print "request-user-2"
    print request_user
    data['proyecto'] = proyecto

    #aca empieza------------------
    todo_rol_asignar = RolAsignar.objects.filter(usuario=usuario_actual.id-1)
    print "todos los roles"
    print todo_rol_asignar
    print "usuario_actual_id"
    print usuario_actual.id
    lista_de_proyectos_del_usuario = []
    for rol_a in todo_rol_asignar:
        lista_de_proyectos_del_usuario.append(rol_a.proyecto)
    print "lista_de_proyectos"
    print lista_de_proyectos_del_usuario
    for verificar in lista_de_proyectos_del_usuario:
        print  "verificar! y proyecto.codigo"
        print verificar.codigo, proyecto.codigo
        if verificar.codigo == proyecto.codigo:
            miembro = True
            break
        miembro = False
    #aca termina------------------
    #if request_user.pk == usuario.pk:
    print "miembro"
    print miembro
    print "request_user=="
    print request_user.pk == usuario.pk
    if miembro is True or request_user.pk == usuario.pk:
        return render(request, template_name, data)
    else:
        return render(request, 'fases/fase_list_sin_permisos.html', {})
"""

@login_required
def fase_list(request, pk, template_name='fases/fase_list.html'):
    #pk= es el primary key del proyecto, YA ESTA
    miembro=False
    fases = Fase.objects.filter(proyecto=pk).order_by('codigo')
    data = {}
    data['object_list'] = fases
    #arreglo temporal
    #recuperamos el proyecto, ahi usamos el lider para que pueda ver las opciones de configurar fases y demas
    proyecto = Proyecto.objects.get(pk=pk)
    usuario_actual = request.user

    #ver_miembro = es_miembro(usuario_actual, proyecto)

    usuario = Usuario.objects.get(pk=proyecto.lider.pk) #este es el usuario lider
    request_user = Usuario.objects.get(username=request.user.username)
    data['proyecto'] = proyecto

    #aca empieza------------------
    todo_rol_asignar = RolAsignar.objects.filter(usuario=usuario_actual.id-1)#esto por el tema que user_admin tiene id=1 y no esta en esa tabla
    lista_de_proyectos_del_usuario = []
    for rol_a in todo_rol_asignar:
        lista_de_proyectos_del_usuario.append(rol_a.proyecto)
    for verificar in lista_de_proyectos_del_usuario:
        if verificar.codigo == proyecto.codigo:
            miembro = True
            break
        miembro = False
    #aca termina------------------
    #if request_user.pk == usuario.pk:
    if miembro is True or request_user.pk == usuario.pk:
        return render(request, template_name, data)
    else:
        return render(request, 'fases/fase_list_sin_permisos.html', {})


@login_required
def fase_create(request, pk, template_name='fases/fase_form.html'):
   #pk= es el primary key del proyecto
    request.POST = request.POST.copy()
    request.POST.__setitem__('proyecto', pk)
    proyecto = Proyecto.objects.get(pk=pk)
    form = FaseForm(request.POST or None)

    if form.is_valid():
        #form.save()
        f = Fase(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], proyecto=proyecto, )
        f.save()
        return redirect('/proyectos/fases/' + pk)
    return render(request, template_name, {'form': form})


@login_required
def fase_update(request, pk, template_name='fases/fase_form.html'):


    fase = get_object_or_404(Fase, pk=pk)
    form = FaseForm(request.POST or None, instance=fase)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form': form})


@login_required
def fase_delete(request, pk, template_name='fases/fase_confirm_delete.html'):
    server = get_object_or_404(Fase, pk=pk)
    proyecto = get_object_or_404(Proyecto,pk=server.proyecto.codigo)
    if request.method == 'POST':
        server.delete()
        return redirect('/proyectos/fases/'+str(proyecto.pk))
    return render(request, template_name, {'object': server})

@login_required
def fase_search(request, pk):
    error = False
    proyecto = Proyecto.objects.get(pk=pk)
    data={}
    data['proyecto'] = proyecto
    data['object_list']={}
    if 'busqueda' in request.GET:
        busqueda = request.GET['busqueda']

        if not busqueda:
            error = True
        else:
            fases= Fase.objects.filter(nombre=busqueda, proyecto = proyecto)
            data['object_list']=fases
            data['query']=busqueda
            return render(request, 'fases/fase_list.html', data)

    return render(request, 'fases/fase_list.html',{'proyecto':proyecto})
