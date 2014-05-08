# -*- coding: ISO-8859-1
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from .models import Atributos
# Create your views here.

class TipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.;'))

    class Meta:
        model = Atributos


@login_required
def tipo_create(request, template_name='tipos/tipo_form.html'):
    form = TipoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form':form})

