from django.shortcuts import redirect
from .carro import Carro
from cursos.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):

    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)

    return redirect("cursos")

def eliminar_producto(request, producto_id):

    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)

    return redirect("cursos")

def restar_producto(request, producto_id):

    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)

    return redirect("cursos")

def limpiar_carro(request, producto_id):

    carro=Carro(request)
    carro.limpiar_carro()

    return redirect("cursos")