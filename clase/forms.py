from django import forms

class Formulario(forms.Form):
    clase = forms.CharField(max_length=20)
    aula = forms.IntegerField()

class BusquedaClase(forms.Form):
    partial_curso = forms.CharField(label='Buscador', max_length=20)

#class BusquedaAula(forms.Form):
    #escribe = forms.CharField(max_length=20)

class BusquedaDatos(forms.Form):
    partial_dato = forms.CharField(label='Buscador', max_length=20)