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

from .models import Proyecto
""" login/views
Se controla lo que va a ser enviado al template para ser mostrado
"""

class ProyectoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.location.href="/proyectos/"'))

    class Meta:
        model = Proyecto
        fields = (
            "nombre",
            "descripcion",
            "fecha_ini",
            "fecha_fin",
            "costo_temporal",
            "costo_monetario",
            "lider",
        )

""" proyecto_list es la funcion que llama al template proyecto_list y se encarga de listar
todos los proyectos existentes"""

@login_required
def proyecto_list(request, template_name='proyectos/proyecto_list.html'):
    proyectos = Proyecto.objects.all().order_by('codigo')
    data = {}
    data['object_list'] = proyectos
    return render(request, template_name, data)

""" Función: proyecto_create
    No recibe parámetros
    Descripción: Solo el usuario administrador del sistema puede crear un proyecto"""
@login_required
def proyecto_create(request, template_name='proyectos/proyecto_form.html'):
    form = ProyectoForm(request.POST or None)
    usuario_administrador=request.user.is_superuser
    if usuario_administrador is True:
        if form.is_valid():
            #f = Proyecto(nombre=request.POST['nombre'], estado="Pendiente",) #estado pendiente por defecto
            #f.save()
            form.save()
            return redirect('lista_proyecto')
        return render(request, template_name, {'form': form})
    else:
        data={}
        data['mensaje'] = "Lo sentimos, Usted no es lider de este proyecto"
        return render(request, 'proyectos/proyecto_list.html', data)

""" Función: proyecto_update
    Parámetros que recibe
    @param: pk
    @value: es el primary key del proyecto
    Descripción: Solo los usuarios Lider o el administrador del proyecto pueden editar las configuraciones iniciales del proyecto, siempre y cuando
    el estado del proyecto sea Pendiente"""
@login_required
def proyecto_update(request, pk, template_name='proyectos/proyecto_form.html'):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    request_user = request.user.id
    usuario_administrador=request.user.is_superuser

    usuario_lider = Usuario.objects.get(pk=proyecto.lider.pk) #este es el usuario lider

    if proyecto.estado == "Pendiente" and request_user == usuario_lider.pk+1 or proyecto.estado == "Pendiente" and usuario_administrador is True: #si el estado es pendiente y si el lider o el admin son los que acceden
        if form.is_valid():
            form.save()
            return redirect('lista_proyecto')
        return render(request, template_name, {'form': form})
    else:

        return render(request, 'proyectos/proyecto_sin_permisos.html', {})

""" Función: proyecto_delete
    Parametros que recibe
    @param: pk
    @value: es el primary key del proyecto
    Descripción: Solo el usuario administrador del proyecto puede eliminar el proyecto siempre y cuando
    el estado sea Pendiente"""
@login_required
def proyecto_delete(request, pk, template_name='proyectos/proyecto_confirm_delete.html'):
    server = get_object_or_404(Proyecto, pk=pk)
    usuario_administrador=request.user.is_superuser
    if server.estado == "Pendiente" and usuario_administrador is True:
        if request.method=='POST':
            server.delete()
            return redirect('lista_proyecto')
        return render(request, template_name, {'object': server})
    else:
        return render(request, 'proyectos/proyecto_sin_permisos.html', {})