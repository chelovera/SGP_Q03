# -*- coding: ISO-8859-1
""" Sistema de Gestión de Proyectos SGP
Grupo Q03
Ingeniería de Software II
@author: Mabel Peña - Alvaro Rodríguez
Año: 2014
"""


from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect

""" login/views
Se controla lo que va a ser enviado al template para ser mostrado
"""
def login(request):
    """
    @param request: recibe un request
    @return: HttpResponse a la pagina de inicio o de proyectos
    """
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return render_to_response('proyectos/index.html')
    else:
        # Show an error page
        return HttpResponse("hiciste algo mal")


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("no se que onda pero ya saliste kp")