from django.urls import path

from .views import nuevo_user, formulario_user, busqueda_user

urlpatterns = [
    path('nueva-aula/', nuevo_user, name='nuevo_user'),
    path('formulario-user/', formulario_user, name='formulario_user'),
    path('busqueda-user/', busqueda_user, name="busqueda_user")
]
