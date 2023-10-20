from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.urls import reverse

class VRegistro(View):

    def get(self, request):
        #form = UserCreationForm()
        form=CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        #form = UserCreationForm(request.POST)
        form=CustomUserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("inicio")
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")

def logear(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")
            usuario=authenticate(username= nombre_usuario, password=contra)
            if usuario is not None: 
                login(request,usuario)
                return redirect('inicio')
            else:
                messages.error(request, "Usuario no valido")
        else:
           messages.error(request, "Informacion incorrecta")
    form= AuthenticationForm()
    return render(request, "login/login.html", {"form":form})

def logearC(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")
            usuario=authenticate(username= nombre_usuario, password=contra)
            if usuario is not None: 
                login(request,usuario)
                admin_url=reverse('admin:index')
                return redirect(admin_url)
            else:
                messages.error(request, "Usuario no valido")
        else:
           messages.error(request, "Informacion incorrecta")
    form= AuthenticationForm()
    return render(request, "loginC/loginC.html", {"form":form})

def logearA(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")
            usuario=authenticate(username= nombre_usuario, password=contra)
            if usuario is not None: 
                login(request,usuario)
                admin_url=reverse('admin:index')
                return redirect(admin_url)
            else:
                messages.error(request, "Usuario no valido")
        else:
           messages.error(request, "Informacion incorrecta")
    form= AuthenticationForm()
    return render(request, "loginA/loginA.html", {"form":form})