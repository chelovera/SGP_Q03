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

@login_required
def proyecto_create(request, template_name='proyectos/proyecto_form.html'):
    form = ProyectoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form': form})

@login_required
def proyecto_update(request, pk, template_name='proyectos/proyecto_form.html'):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form': form})

@login_required
def proyecto_delete(request, pk, template_name='proyectos/proyecto_confirm_delete.html'):
    server = get_object_or_404(Proyecto, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('lista_proyecto')
    return render(request, template_name, {'object': server})
