from django.http import HttpResponse
import random
from django.shortcuts import render
from django.contrib.auth import login as django_login, authenticate
from .forms import NuestraCreacionUser, NuestraEdicionUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.template import loader


def inicio(request):
    return render(request, "indice/index.html", {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Regresa a la pagina anterior</h1>
                        ''')

def acercademi(request):

    nombre = 'Natalia'
    apellido = 'Lin'
    pais = 'Peru'
    proyecto = 'Este proyecto es una web semejante a un Blog'

    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'pais': pais,
        'nombre_largo': len(nombre),
        'proyecto': proyecto
    }

    return render(request, "indice/acercademi.html", diccionario_de_datos)

def pages(request):
    
    titulo = 'Blog Uno'

    diccionario_de_datos = {
        'titulo': titulo,
    }

    return render(request, "indice/pages.html", diccionario_de_datos)

def pagesid(request):
    subtitulo = 'Subtitulo Uno'
    autor = 'Autor'
    cuerpo = 'Cuerpo'
    fecha = 'Fecha'

    diccionario_de_datos = {
        'subtitulo': subtitulo,
        'autor': autor,
        'cuerpo': cuerpo,
        'fecha': fecha
    }

    return render(request, "indice/pages.html", diccionario_de_datos)

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                django_login(request, user)
                return render(request, 'indice/index.html', {'msj': 'Te logueaste!'})
            else:
                return render(request, 'indice/login.html', {'form': form, 'msj': 'No se autenticó'})
        
        else:
            return render(request, 'indice/login.html', {'form': form, 'msj': 'datos con formato incorrecto'})
    else:    
        form = AuthenticationForm()
        return render(request, 'indice/login.html', {'form': form, 'msj': ''})

def registrar(request):
    
    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'indice/index.html', {'msj': f'Se creo el user {username}'})
        else:
            return render(request, 'indice/registrar.html', {'form': form, 'msj': ''})

    form = NuestraCreacionUser()
    return render(request, 'indice/registrar.html', {'form': form, 'msj': ''})

@login_required
def editar(request):
    msj = ''
    if request.method == 'POST':
        form = NuestraEdicionUser(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            logued_user = request.user
            logued_user.email= data.get('email')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name', '')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                logued_user.set_password(data.get('password1'))
            else:
                msj = 'No se modifico el password.'

            logued_user.save()

            return render(request, 'indice/index.html', {'msj': msj, 'user_avatar_url': buscar_url_avatar(request.user)})
        else:
            return render(request, 'indice/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': buscar_url_avatar(request.user)})

    form = NuestraEdicionUser(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'user_name': request.user.username
        }
    )
