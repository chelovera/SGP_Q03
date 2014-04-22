from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario

@login_required
def usuario_list(request, template_name='usuarios/usuario_list.html'):
    usuarios = Usuario.objects.all()
    data = {}
    data['object_list'] = usuarios
    return render(request, template_name, data)

@login_required
def usuario_create(request, template_name='usuarios/usuario_form.html'):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_usuario')
    return render(request, template_name, {'form':form})

@login_required
def usuario_update(request, pk, template_name='usuarios/usuario_form.html'):
    usuario = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('lista_usuario')
    return render(request, template_name, {'form':form})

@login_required
def usuario_delete(request, pk, template_name='usuarios/usuario_confirm_delete.html'):
    server = get_object_or_404(Usuario, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('lista_usuario')
    return render(request, template_name, {'object':server})
