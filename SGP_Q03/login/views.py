from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

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
        return HttpResponse("loco hiciste algo mal")


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("no se que onda pero ya saliste kp")