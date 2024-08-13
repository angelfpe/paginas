# pirrin/urls.py

from django.contrib import admin
from django.urls import path
from myapp import views  # Importa las vistas de myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contacto, name='contacto'),  # Define la URL para la vista de contacto
]
