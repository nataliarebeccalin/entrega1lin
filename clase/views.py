from django.http import HttpResponse
from django.shortcuts import render, redirect
from clase.models import User, Datos, Blog
from clase.forms import Formulario, BusquedaUser, BlogFormulario
from django.contrib.auth.decorators import login_required
import random  

def nuevo_user(request):
    user = random.randrange(0, 50)
    nuevo_user = User(nombre=user['nombre'], apellido=user['apellido'], edad=user['edad'], email=user['email'])
    nuevo_user.save()
    return HttpResponse(f"Se creo el user {nuevo_user.nombre} {nuevo_user.apellido} edad {nuevo_user.user} correo {nuevo_user.email}")

def formulario_user(request):
    if request.method == 'POST':
        formulario = Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_user = User(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'], email=data['email'])
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

def listado_blog(request):
    listado_blog = Blog.objects.all()
    return render(
        request, "clase/listado_blog.html", 
        {'listado_blog': listado_blog}
    )

@login_required
def crear_blog(request):
    if request.method == 'POST':
        formulario = BlogFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_blog = Blog(
                titulo=data['titulo'], 
                subtitulo=data['subtitulo'],
                cuerpo=data['cuerpo'],
                autor=data['autor'],
                fecha=data['fecha']
            )
            nuevo_blog.save()
            return redirect('listado_blog')


    formulario = BlogFormulario()
    return render(
        request, 'clase/crear_blog.html', 
        {'formulario': formulario}
    )

def actualizar_blog(request, id):

    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        formulario = BlogFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            blog.titulo = data['nombre']
            blog.subtitulo = data['subtitulo']
            blog.cuerpo=data['cuerpo']
            blog.autor=data['autor']
            blog.fecha=data['fecha']
            blog.save()
            return redirect('listado_blog')

    formulario = BlogFormulario(
        initial={
            'titulo': blog.titulo,
            'subtitulo': blog.subtitulo,
            'cuerpo': blog.cuerpo,
            'autor': blog.autor,
            'fecha': blog.fecha,
        }
    )
    return render(
        request, 'clase/actualizar_blog.html', 
        {'formulario': formulario, 'blog': blog}
    )

def borrar_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('listado_blog')