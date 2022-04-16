from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class BusquedaUser(forms.Form):
    partial_user = forms.CharField(label='Buscador', max_length=20)

#class BusquedaAula(forms.Form):
    #escribe = forms.CharField(max_length=20)
