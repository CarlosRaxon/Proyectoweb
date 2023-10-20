from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'proyectowebapp/Inicio.html')

def about(request):
    return render(request, 'proyectowebapp/about.html')
