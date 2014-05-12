# -*- coding: ISO-8859-1
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from .models import Atributo
from .models import Tipo_Item
from usuarios.models import Usuario
from fases.models import Fase
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
        model = Tipo_Item
        exclude=("fase",)



@login_required
def tipo_create(request, pk, template_name='tipos/tipo_form.html'):
    fase=Fase.objects.get(pk=pk)
    form = TipoForm(request.POST or None)

    if form.is_valid():
        tipo_item = Tipo_Item(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], fase=fase,)
        tipo_item.save()
        return redirect('/proyectos/fases/tipo_item/'+pk)
    return render(request, template_name, {'form': form})

@login_required
def tipo_list(request, pk, template_name='tipos/tipos_list.html'):
    tipos = Tipo_Item.objects.filter(fase=pk).order_by('codigo')
    data = {}
    data['object_list'] = tipos
    #arreglo temporal
    #recuperamos el proyecto, ahi usamos el lider para que pueda ver las opciones de configurar fases y demas
    usuario = Usuario.objects.get(pk=Fase.objects.get(pk=pk).proyecto.lider.pk)
    request_user = Usuario.objects.get(username=request.user.username)
    data['fase'] = Fase.objects.get(pk=pk)
    if request_user.pk == usuario.pk:
        return render(request, template_name, data)
    else:
        return render(request, 'fases/fase_list.html', {})