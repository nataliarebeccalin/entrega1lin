from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Aula
from clase.forms import Formulario, BusquedaClase
import random  

def nueva_aula(request):
    aula = random.randrange(0, 50)
    nueva_aula = Aula(nombre='Aula Clases', aula=aula)
    nueva_aula.save()
    return HttpResponse(f"Se creo el aula {nueva_aula.nombre} aula {nueva_aula.aula}")

def formulario_clase(request):
    if request.method == 'POST':
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_aula = Aula(nombre=data['curso'], aula=data['aula'])
            nueva_aula.save()
            return render(request, 'indice/index.html', {'nuevo_curso': nueva_aula})

    formulario = Formulario
    return render(request, 'clase/formulario_clase.html', {'formulario': formulario})

def busqueda_clase(request):
    clases_buscadas = []
    dato = request.GET.get('partial_curso', None)

    if dato is not None:
        clases_buscadas = Aula.objects.filter(nombre__icontains=dato)

    buscador = BusquedaClase()
    return render(
        request, "clase/busqueda_clase.html", 
        {'buscador': buscador, 'clases_buscadas': clases_buscadas, 'dato': dato}
        )