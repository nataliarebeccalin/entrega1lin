from django.urls import path

from .views import nueva_aula, formulario_clase, busqueda_clase

urlpatterns = [
    path('nueva-aula/', nueva_aula, name='nueva_aula'),
    path('formulario-clase/', formulario_clase, name='formulario_clase'),
    path('busqueda-clase/', busqueda_clase, name="busqueda_clase")
]
