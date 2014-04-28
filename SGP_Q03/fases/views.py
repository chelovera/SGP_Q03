# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

from .models import Fase


class FaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FaseForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.location.href="#"'))

    class Meta:
        model = Fase


@login_required
def fase_list(request, pk ,  template_name='fases/fase_list.html'):
    fases = Fase.objects.filter(proyecto=pk)
    data = {}
    data['object_list'] = fases
    return render(request, template_name, data)

@login_required
def fase_create(request, template_name='fases/fase_form.html'):
    form = FaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_fase')
    return render(request, template_name, {'form':form})

@login_required
def  fase_update(request, pk, template_name='fases/fase_form.html'):
    fase = get_object_or_404(Fase, pk=pk)
    form = FaseForm(request.POST or None, instance=fase)
    if form.is_valid():
        form.save()
        return redirect('lista_fase')
    return render(request, template_name, {'form':form})

@login_required
def fase_delete(request, pk, template_name='fases/fase_confirm_delete.html'):
    server = get_object_or_404(Fase, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('lista_fase')
    return render(request, template_name, {'object':server})
