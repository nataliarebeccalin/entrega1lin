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
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"

class Blog(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=80)
    autor = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return f"Titulo: {self.titulo}"