# myapp/admin.py

from django.contrib import admin
from .models import Contacto

# Registro del modelo Contacto en el sitio de administración
admin.site.register(Contacto)
