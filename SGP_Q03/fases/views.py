# -*- coding: ISO-8859-1
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Hidden

from .models import Fase
from usuarios.models import Usuario
from proyectos.models import Proyecto

class FaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FaseForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # para que no renderice el <form></form>
        #self.helper.form_tag = False
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.;'))

    def clean_proyecto(self):
        """
        @param self: se ejecuta sobre un formulario para asignarle un proyecto
        @return: se retorna el proyecto de la fase
        """
        proyecto=self.cleaned_data['proyecto']
        proyecto=Proyecto.objects.get(codigo=proyecto.codigo)
        return proyecto

    class Meta:
        model = Fase
        fields = (
            "nombre",
            "descripcion",
            #"proyecto",
            "fecha_ini",
            "fecha_fin",
            "costo_temporal",
            "costo_monetario",
        )

@login_required
def fase_list(request, pk ,  template_name='fases/fase_list.html'):
    fases = Fase.objects.filter(proyecto=pk)
    data = {}
    data['object_list'] = fases
    #arreglo temporal
    #recuperamos el proyecto, ahi usamos el lider para que pueda ver las opciones de configurar fases y demas
    proyecto = Proyecto.objects.get(pk=pk)
    usuario = Usuario.objects.get(pk=proyecto.lider.pk)
    request_user= Usuario.objects.get(nombre=request.user.username)
    data['proyecto']=proyecto
    if request_user.pk == usuario.pk:
        return render(request, template_name, data)
    else:
        return render(request, 'fases/fase_list.html', {})


@login_required
def fase_create(request,pk, template_name='fases/fase_form.html'):
    """

    :param request:
    :param pk:
    :param template_name:
    :return:
    """
    request.POST=request.POST.copy()
    request.POST.__setitem__('proyecto',pk)
    proyecto=Proyecto.objects.get(pk=pk)
    form = FaseForm(request.POST or None)

    if form.is_valid():
        #form.save()
        f = Fase(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'],proyecto=proyecto,)
        f.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form':form})


@login_required
def  fase_update(request, pk, template_name='fases/fase_form.html'):
    """

    :param request:
    :param pk:
    :param template_name:
    :return:
    """
    fase = get_object_or_404(Fase, pk=pk)
    form = FaseForm(request.POST or None, instance=fase)
    if form.is_valid():
        form.save()
        return redirect('lista_proyecto')
    return render(request, template_name, {'form':form})

@login_required
def fase_delete(request, pk, template_name='fases/fase_confirm_delete.html'):
    server = get_object_or_404(Fase, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('lista_fase')
    return render(request, template_name, {'object':server})
