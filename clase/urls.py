from django.urls import path

from . import views

urlpatterns = [
    path('nuevo/', views.nuevo_user, name='nuevo_user'),
    path('formulario-user/', views.formulario_user, name='formulario_user'),
    path('busqueda-user/', views.busqueda_user, name="busqueda_user"),

    path('blog/listado/', views.listado_blog, name='listado_blog'),

    path('blog/crear/', views.crear_blog, name='crear_blog'),
    path('blog/borrar/<int:id>/', views.borrar_blog, name='borrar_blog'),
    path('blog/actualizar/<int:id>/', views.actualizar_blog, name='actualizar_blog'),
]
