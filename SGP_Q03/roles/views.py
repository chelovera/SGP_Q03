from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

from .models import Rol

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


@login_required
def rol_list(request, template_name='roles/rol_list.html'):
    roles = Rol.objects.all()
    data = {}
    data['object_list'] = roles
    return render(request, template_name, data)

@login_required
def rol_create(request, template_name='roles/rol_form.html'):
    form = RolForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_rol')
    return render(request, template_name, {'form':form})

@login_required
def  rol_update(request, pk, template_name='roles/rol_form.html'):
    rol = get_object_or_404(Rol, pk=pk)
    form = RolForm(request.POST or None, instance=rol)
    if form.is_valid():
        form.save()
        return redirect('lista_rol')
    return render(request, template_name, {'form':form})

@login_required
def rol_delete(request, pk, template_name='roles/rol_confirm_delete.html'):
    server = get_object_or_404(Rol, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('lista_rol')
    return render(request, template_name, {'object':server})
