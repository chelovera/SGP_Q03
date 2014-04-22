from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Proyecto

class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto

@login_required
def proyecto_list(request, template_name='proyectos/proyecto_list.html'):
    proyectos = Proyecto.objects.all()
    data = {}
    data['object_list'] = proyectos
    return render(request, template_name, data)

@login_required
def proyecto_create(request, template_name='proyectos/proyecto_form.html'):
    form = ProyectoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form':form})

@login_required
def  proyecto_update(request, pk, template_name='proyectos/proyecto_form.html'):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    form = ProyectoForm(request.POST or None, instance=proyecto)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form':form})

@login_required
def proyecto_delete(request, pk, template_name='proyectos/proyecto_confirm_delete.html'):
    server = get_object_or_404(Usuario, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('proyecto_usuario')
    return render(request, template_name, {'object':server})
