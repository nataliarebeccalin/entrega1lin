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

def numero_random(request):
    numero = random.randrange(1, 200)
    texto = f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def nombre_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)

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