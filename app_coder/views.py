from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):

    return render(request ,"app_coder/inicio.html")

def cursos(request):

    return render(request ,"app_coder/cursos.html")

def profesores(request):

    return render(request ,"app_coder/profesores.html")

def estudiantes(request):

    return render(request ,"app_coder/estudiantes.html")

def entregables(request):

    return render(request ,"app_coder/entregables.html")