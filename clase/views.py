from django.http import HttpResponse
from django.shortcuts import render
from clase.models import User, Datos
from clase.forms import Formulario, BusquedaUser
import random  

def nuevo_user(request):
    user = random.randrange(0, 50)
    nuevo_user = User(nombre=user['nombre'], apellido=user['apellido'], edad=user['edad'])
    nuevo_user.save()
    return HttpResponse(f"Se creo el user {nuevo_user.nombre} {nuevo_user.apellido} edad {nuevo_user.user}")

def formulario_user(request):
    if request.method == 'POST':
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_user = User(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'])
            nuevo_user.save()
            return render(request, 'indice/index.html', {'nuevo_user': nuevo_user})

    formulario = Formulario
    return render(request, 'clase/formulario_user.html', {'formulario': formulario})

def busqueda_user(request):
    user_buscado = []
    nombre = request.GET.get('partial_user', None)

    if nombre is not None:
        user_buscado = User.objects.filter(nombre__icontains=nombre)

    buscador = BusquedaUser()
    return render(
        request, "clase/busqueda_user.html", 
        {'buscador': buscador, 'user_buscado': user_buscado, 'nombre': nombre}
        )

