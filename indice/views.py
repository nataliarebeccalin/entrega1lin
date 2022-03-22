from django.http import HttpResponse
import random
from django.shortcuts import render


from django.template import loader


def inicio(request):
    return render(request, "indice/index.html", {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Regresa a la pagina anterior</h1>
                        ''')

def mi_plantilla(request):

    nombre = 'Natalia'
    apellido = 'Lin'
    pais = 'Peru'

    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'pais': pais,
        'nombre_largo': len(nombre)
    }

    return render(request, "indice/mi_plantilla.html", diccionario_de_datos)