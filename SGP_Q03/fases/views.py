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



@login_required
def fase_list(request, pk, template_name='fases/fase_list.html'):
    """
    Función: fase_list
        Parámetros que recibe
    @param: pk
    @value: es el primary key del proyecto
        Descripción: Solo los usuarios Lider y miembros del proyecto pueden tener acceso a las funcionalidades del proyecto
    """

    #pk= es el primary key del proyecto, YA ESTA ESTO
    request_user = Usuario.objects.get(username=request.user.username)
    proyecto = Proyecto.objects.get(pk=pk) #recuperamos el proyecto
    usuario_lider = Usuario.objects.get(pk=proyecto.lider.pk) #este es el usuario lider
    aux_proyecto = proyecto  #asignamos para poder recuperar todos los campos ingresados anteriormente
    if proyecto.estado == "Pendiente" and request_user.pk == usuario_lider.pk:    #si es lider y se listan las fases por primera vez, entonces el estado del proyecto = iniciado
        p = Proyecto(codigo=aux_proyecto.codigo, nombre=aux_proyecto.nombre, descripcion=aux_proyecto.descripcion, estado="Iniciado", fecha_ini=aux_proyecto.fecha_ini, fecha_fin=aux_proyecto.fecha_fin, costo_temporal=aux_proyecto.costo_temporal, costo_monetario=aux_proyecto.costo_monetario, lider=request_user)
        p.save()
        #Proyecto.estado = "Iniciado"
    miembro=False
    fases = Fase.objects.filter(proyecto=pk).order_by('codigo')
    data = {}
    data['object_list'] = fases

    usuario_actual = request.user

    #ver_miembro = es_miembro(usuario_actual, proyecto)

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
    #if request_user.pk == usuario_lider.pk:
    if miembro is True or request_user.pk == usuario_lider.pk:
        return render(request, template_name, data)
    else:
        data={}
        data['mensaje'] = "Lo sentimos, Usted no es miembro de este proyecto"
        data['proyecto']=proyecto
        return render(request, 'fases/fase_list_sin_permisos.html', data)

@login_required
def fase_create(request, pk, template_name='fases/fase_form.html'):
    """
    Función: fase_create
        Parametros que recibe
    @param: pk
    @value: es el primary key del proyecto
        Descripción: Solo el usuario Lider del proyecto puede crear una fase en el proyecto

    """

    #pk= es el primary key del proyecto YA ESTA ESTO
    request.POST = request.POST.copy()
    request.POST.__setitem__('proyecto', pk)
    proyecto = Proyecto.objects.get(pk=pk)
    form = FaseForm(request.POST or None)
    usuario_actual = request.user
    usuario_lider = Usuario.objects.get(pk=proyecto.lider.pk)
    request_user = Usuario.objects.get(username=request.user.username)
    if request_user.pk == usuario_lider.pk:
        if form.is_valid():
            #form.save()
            f = Fase(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], proyecto=proyecto, )
            f.save()
            return redirect('/proyectos/fases/' + pk)
        return render(request, template_name, {'form': form})
    else:
        return render(request, 'fases/fase_list_sin_permisos.html', {})

@login_required
def fase_update(request, pk, template_name='fases/fase_form.html'):
    #esta funcion no se usa

    fase = get_object_or_404(Fase, pk=pk)
    form = FaseForm(request.POST or None, instance=fase)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form': form})


@login_required
def fase_finalizar(request, pk, template_name='proyectos/proyecto_list.html'):
    """
    Función: fase_finalizar
        Parametros que recibe
    @param fase_finalizar: pk
    @value: es el primary key de la fase
    @return Descripción: Solo el lider puede finalizar un proyecto
    """

    #Todavia falta con lo que despues implementemos, cambiar la redireccion del template
    server = get_object_or_404(Fase, pk=pk)
    usuario_lider=server.proyecto.lider
    usuario_actual=request.user.id

    if usuario_lider.pk+1== usuario_actual:
        aux_fase=server
        p = Fase(codigo=aux_fase.codigo, nombre=aux_fase.nombre, descripcion=aux_fase.descripcion, estado="Cerrada", proyecto=aux_fase.proyecto, fecha_ini=aux_fase.fecha_ini, fecha_fin=aux_fase.fecha_fin, costo_temporal=aux_fase.costo_temporal, costo_monetario=aux_fase.costo_monetario, orden=aux_fase.orden)
        p.save()
        return redirect('lista_proyecto')
    else:
        data={}
        data['mensaje'] = "Lo sentimos, Usted no es lider de este proyecto"
        return render(request, template_name, data)



@login_required
def fase_delete(request, pk, template_name='fases/fase_confirm_delete.html'):
    """
    Función: fase_delete
        Parametros que recibe
    @param: pk
    @value: es el primary key de la fase
        Descripción: Solo el lider puede eliminar una fase siempre y cuando la fase este en estado abierta
    """
    #volver a mirar la logica del borrado
    server = get_object_or_404(Fase, pk=pk)

    usuario_lider = server.proyecto.lider
    print usuario_lider

    usuario_actual = Usuario.objects.get(username=request.user.username)
    print usuario_actual
    if server.estado=="Abierta" and usuario_actual.pk==usuario_lider.pk:
        proyecto = get_object_or_404(Proyecto,pk=server.proyecto.codigo)
        if request.method == 'POST':
            server.delete()
            return redirect('/proyectos/fases/'+str(proyecto.pk))
        return render(request, template_name, {'object': server})
    else:
        data = {}
        data['mensaje']="lo siento, no puede realizar esta accion"
        return render(request, 'fases/fase_list_sin_permisos.html', data)

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
