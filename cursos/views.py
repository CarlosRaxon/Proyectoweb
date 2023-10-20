from django.shortcuts import render
from cursos.models import Producto

# Create your views here.

def cursos(request):
    productos=Producto.objects.all()
    return render(request, 'cursos/cursos.html', {"productos": productos})