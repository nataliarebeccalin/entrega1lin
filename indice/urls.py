from django.urls import path
from .views import inicio, otra_vista, mi_plantilla

urlpatterns = [
    path('', inicio, name="inicio"),
    path('otra-vista/', otra_vista, name="otra_vista"),
    path('mi-plantilla/', mi_plantilla, name="mi_plantilla"),  
]