from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Usuario


#@login_required
class UsuarioLista(ListView):
    model = Usuario

#@login_required
class UsuarioCrear(CreateView):
    model = Usuario
    success_url = reverse_lazy('lista_usuarios')

#@login_required
class UsuarioModificar(UpdateView):
    model = Usuario
    success_url = reverse_lazy('lista_usuarios')

#@login_required
class UsuarioBorrar(DeleteView):
    model = Usuario
    success_url = reverse_lazy('lista_usuarios')


