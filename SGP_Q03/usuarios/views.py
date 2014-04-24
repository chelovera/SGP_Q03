from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-primary pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.location.href="/usuarios/"'))

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


@login_required
def search(request):
    error = False
    if 'busqueda' in request.GET:
        busqueda = request.GET['busqueda']
        if not busqueda:
            error = True
        else:
            usuarios = Usuario.objects.filter(username=busqueda)
            return render(request, 'usuarios/search_results.html',
                {'usuarios': usuarios, 'query': busqueda})
    return render(request, 'usuarios/search_form.html',
        {'error': error})
