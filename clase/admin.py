from django.contrib import admin

from .models import Alumnos, Profesores, Aula

# Register your models here.

admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Aula)
