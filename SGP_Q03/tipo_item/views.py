# -*- coding: ISO-8859-1
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from .models import Atributo, Tipo_Item, Item
from usuarios.models import Usuario
from fases.models import Fase
from roles.models import Rol, RolAsignar

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

""" Función: tipo_create
    Parámetros que recibe
    @param: pk
    @value: es el primary key de la fase
    Descripción: solo los que tengan permisos para crear_tipo_item en esta fase del proyecto pueden acceder ademas del
    usuario lider"""


@login_required
def tipo_create(request, pk, template_name='tipos/tipo_form.html'):
    posee_permiso=0
    #refinar=hacer que sean roles por fase, ahora mismo se manejan en esta funcion roles por proyecto
    fase=Fase.objects.get(pk=pk)
    form = TipoForm(request.POST or None)
    usuario_lider = Usuario.objects.get(pk=Fase.objects.get(pk=pk).proyecto.lider.id)#lider
    print usuario_lider.id
    usuario_actual = Usuario.objects.get(username=request.user.username)#usuario_actual
    print usuario_actual.id
    lista_de_roles_del_usuario = []
    todos_los_roles_usuario = RolAsignar.objects.filter(usuario=usuario_actual, proyecto=fase.proyecto.pk)#roles del usuario dentro de esa fase
    print todos_los_roles_usuario
    for rol_a in todos_los_roles_usuario:
        lista_de_roles_del_usuario.append(rol_a.rol)
    #print usuario_actual

    for rol_a in lista_de_roles_del_usuario:
        posee_permiso=len(Rol.objects.filter(codigo=rol_a.codigo, nombre=rol_a.nombre, crear_tipo_item=True))
        if posee_permiso>0:# si en al menos uno de sus roles posee el permiso crear_tipo_item
            break
    #print posee_permiso
    #print todos_los_roles_usuario
    if posee_permiso>=1 or usuario_actual.id == usuario_lider.id:
        if form.is_valid():
            tipo_item = Tipo_Item(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], fase=fase,)
            tipo_item.save()
            return redirect('/proyectos/fases/tipo_item/'+pk)
        return render(request, template_name, {'form': form})
    else:
        data={}
        data['mensaje']="lo sentimos, ud no puede crear tipo de item"
        return render(request, 'tipos/tipo_sin_permisos.html', data)

@login_required
def tipo_update(request, pk, template_name='tipos/tipo_form.html'):
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

""" Función: tipo_list
    Parámetros que recibe
    @param: pk
    @value: es el primary key de la fase
    Descripción: solo los que tengan permisos para crear_tipo_item, editar_tipo_item o eliminar_tipo_item pueden ver que tipo de item existen en la fase de manera a informarse para
    poder utilizarlos """
@login_required
def tipo_list(request, pk, template_name='tipos/tipos_list.html'):
    posee_permiso=0
    tipos = Tipo_Item.objects.filter(fase=pk).order_by('codigo')
    data = {}
    data['object_list'] = tipos
    fase=Fase.objects.get(pk=pk)
    data['fase']=fase
    usuario_lider = Usuario.objects.get(pk=Fase.objects.get(pk=pk).proyecto.lider.pk)#lider
    usuario_actual = Usuario.objects.get(username=request.user.username)#usuario_actual
    #print usuario_actual
    lista_de_roles_del_usuario = []
    todos_los_roles_usuario = RolAsignar.objects.filter(usuario=usuario_actual, proyecto=fase.proyecto.pk)#roles del usuario dentro de esa fase
    for rol_a in todos_los_roles_usuario:
        lista_de_roles_del_usuario.append(rol_a.rol)
    #print lista_de_roles_del_usuario

    for rol_a in lista_de_roles_del_usuario:
        #posee_permiso=(len(Rol.objects.filter(codigo=rol_a.codigo, nombre=rol_a.nombre, crear_tipo_item=True))+len(Rol.objects.filter(codigo=rol_a.codigo, nombre=rol_a.nombre, editar_tipo_item=True))+len(Rol.objects.filter(codigo=rol_a.codigo, nombre=rol_a.nombre, eliminar_tipo_item=True)))
        posee_permiso=len(Rol.objects.filter(codigo=rol_a.codigo, nombre=rol_a.nombre, crear_tipo_item=True))
        #print posee_permiso
        if posee_permiso>0:# si en al menos uno de sus roles posee el permiso crear_tipo_item
            break
   #print posee_permiso
    #print todos_los_roles_usuario
    #print usuario_actual.pk
    #print usuario_lider.pk
    if posee_permiso>=1 or usuario_actual.pk == usuario_lider.pk:
        return render(request, template_name, data)
    else:
        data['mensaje']="lo sentimos, ud no tiene el permiso correpondiente"
        return render(request, 'tipos/tipo_sin_permisos.html', data)

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