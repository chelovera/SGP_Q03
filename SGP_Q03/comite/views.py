__author__ = 'penhagonzalez'

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from proyectos.models import Proyecto
from usuarios.models import Usuario
from .models import Comite


class FormComite(ModelForm):

    class Meta:
        model = Comite
        fields = "miembros"

    def __init__(self, *args, **kwargs):

        super(FormComite, self).__init__(*args, **kwargs)

        self.fields["miembros"].widget = CheckboxSelectMultiple()
        self.fields["miembros"].queryset = Usuario.objects.all()


""" Inicio de las Funciones relacionadas con Comite"""
@login_required
def comite_create(request, pk, template_name='fases/comite.html'):
    """ pk=es el primary key del proyecto"""
    request.POST = request.POST.copy()
    request.POST.__setitem__('proyecto', pk)
    proyecto=Proyecto.objects.get(pk=pk)
    lider=proyecto.lider
    form = FormComite(request.POST or None)
    if form.is_valid():
        r = Comite(proyecto=proyecto, miembro_uno=lider, miembros=request.POST['miembros'])
        r.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form': form})




"""
def fase_create(request, pk, template_name='fases/fase_form.html'):
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
"""
