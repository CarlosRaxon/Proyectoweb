from django.urls import path
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Inicio/', views.inicio, name='inicio'),
    path('Sobre_nosotros/', views.about, name='about'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)