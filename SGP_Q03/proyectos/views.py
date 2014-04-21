from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def index(resquest):
    return render_to_response('proyectos/proyectos.html')
