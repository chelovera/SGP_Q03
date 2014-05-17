# -*- coding: ISO-8859-1
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from .models import Atributo, Tipo_Item, Item
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

class AtributoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AtributoForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.;'))

    class Meta:
        model = Atributo
        exclude=("tipo_item",)

class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.help_text_inline = True
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('guardar', 'guardar', css_class='btn btn-large btn-success pull-left'))
        self.helper.add_input(Button('cancelar', 'cancelar', css_class='btn btn-large btn-danger', onclick='window.;'))

    class Meta:
        model = Item

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
def  tipo_update(request, pk, template_name='tipos/tipo_form.html'):
    tipo_item = get_object_or_404(Tipo_Item, pk=pk)
    fase=tipo_item.fase
    data={}
    data['fase']=fase
    data['object_list']=Tipo_Item.objects.filter(fase=pk).order_by('codigo')
    form = TipoForm(request.POST or None, instance=tipo_item)
    if form.is_valid():
        form.save()
        return redirect('/proyectos/fases/tipo_item/'+str(fase.codigo))
    return render(request, template_name, {'form':form})

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

@login_required
def atributo_list(request, pk, template_name='tipos/atributos_list.html'):
    atributos = Atributo.objects.filter(tipo_item=pk).order_by('codigo')
    data = {}
    data['object_list'] = atributos
    #arreglo temporal
    #recuperamos el proyecto, ahi usamos el lider para que pueda ver las opciones de configurar fases y demas
    #falta determinar si el usuario es miembro del proyecto
    #usuario = Usuario.objects.get(pk=Fase.objects.get(pk=pk).proyecto.lider.pk)
    usuario= Usuario.objects.get(username=request.user.username)
    request_user = Usuario.objects.get(username=request.user.username)
    data['tipo'] = Tipo_Item.objects.get(pk=pk)
    if request_user.pk == usuario.pk:
        return render(request, template_name, data)
    else:
        return render(request, '500.html', {})

@login_required
def atributo_create(request, pk, template_name='tipos/atributo_form.html'):
    tipo_item = Tipo_Item.objects.get(pk=pk)
    form = AtributoForm(request.POST or None)

    if form.is_valid():
        atributo = Atributo(nombre=request.POST['nombre'], tipo=request.POST['tipo'], tipo_item=tipo_item,)
        atributo.save()
        return redirect('/proyectos/fases/tipo_item/atributos/'+pk)
    return render(request, template_name, {'form': form})

@login_required
def tipo_delete(request, pk, template_name='tipos/tipo_confirm_delete.html'):
    server = get_object_or_404(Tipo_Item, pk=pk)
    fase = get_object_or_404(Fase, pk=server.fase.codigo)
    if request.method == 'POST':
        server.delete()
        return redirect('/proyectos/fases/tipo_item/'+str(fase.pk))
    return render(request, template_name, {'object': server})

@login_required
def atributo_delete(request, pk, template_name='tipos/tipo_confirm_delete.html'):
    atributo = get_object_or_404(Atributo, pk=pk)
    tipo_item = get_object_or_404(Tipo_Item, pk=atributo.tipo_item.codigo)
    items = Item.objects.filter(tipo_item=tipo_item)
    if not items:
        #if request.method == 'POST':
        atributo.delete()
        return redirect('/proyectos/fases/tipo_item/atributos/'+str(tipo_item.pk))
    return render(request,('error.html'), {'object': atributo,'error_atributo':True})

@login_required
def item_create(request, pk, template_name='tipos/item_form.html'):
    fase = Fase.objects.get(pk=pk)

    form = ItemForm(request.POST or None)
    if form.is_valid():
        tipo_item= get_object_or_404(Tipo_Item, pk=request.POST.get('tipo_item'))
        item = Item(nombre=request.POST['nombre'], costo=request.POST['costo'], dificultad=request.POST['dificultad'],tipo_item= tipo_item, fase=fase, actual=True )
        item.save()
        atributos=Atributo.objects.filter(tipo_item=tipo_item) & Atributo.objects.filter(item=None)
        for atributo in atributos:
            nuevo_atributo=Atributo(nombre=atributo.nombre, tipo=atributo.tipo, tipo_item=tipo_item, item=item)
            nuevo_atributo.save()
        return redirect('/proyectos/fases/tipo_item/items/'+pk)
    return render(request, template_name, {'form': form})

@login_required
def item_list(request, pk, template_name='tipos/item_list.html'):
    items = Item.objects.filter(fase=pk).order_by('codigo')
    data = {}
    data['object_list'] = items
    fase= Fase.objects.get(pk=pk)
    data['fase']=fase
    #arreglo temporal
    #recuperamos el proyecto, ahi usamos el lider para que pueda ver las opciones de configurar fases y demas
    #falta determinar si el usuario es miembro del proyecto
    #usuario = Usuario.objects.get(pk=Fase.objects.get(pk=pk).proyecto.lider.pk)
    usuario= Usuario.objects.get(username=request.user.username)
    request_user = Usuario.objects.get(username=request.user.username)
    data['fase'] = Fase.objects.get(pk=pk)
    if request_user.pk == usuario.pk:
        return render(request, template_name, data)
    else:
        return render(request, '500.html', {})