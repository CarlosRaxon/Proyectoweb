from django.urls import path
from . import views

urlpatterns = [
    path('Contactanos/', views.contactanos, name='contactanos'),
]

