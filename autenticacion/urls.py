from django.urls import path
from .views import VRegistro, cerrar_sesion, logear, logearC, logearA

urlpatterns = [
    path('Autenticacion/', VRegistro.as_view(), name='autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='logout'),
    path('logear', logear, name='logear'),
    path('logearC', logearC, name='logearC'),
    path('logearA', logearA, name='logearA'),
]

