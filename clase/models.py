from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesión = models.CharField(max_length=30)

class Datos(models.Model):
    nombre = models.CharField(max_length=20)
    dato = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Dato: {self.dato}"

class Aula(models.Model):
    nombre = models.CharField(max_length=20)
    aula = models.IntegerField()

    def __str__(self):
        return f"Clase: {self.nombre} - Aula: {self.aula}"