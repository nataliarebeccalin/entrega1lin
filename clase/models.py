from django.db import models

# Create your models here.

class Datos(models.Model):
    nombre = models.CharField(max_length=20)
    dato = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Dato: {self.dato}"

class User(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Email: {self.email}"

class Blog(models.Model):
    titulo = "Blog 1"
    subtitulo = "Subtitulo 1"
    cuerpo = "Cuerpo 1"
    autor = "Autor: Natalia Lin"
    fecha = "Abril 2022"