from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Bloguno(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=80)
    autor = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return f"Titulo: {self.titulo}"

class Blogdos(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=80)
    autor = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Titulo: {self.titulo}"
