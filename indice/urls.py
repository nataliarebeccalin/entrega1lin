from django.urls import path
from .views import inicio, otra_vista, acercademi, login, registrar, editar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('otra-vista/', otra_vista, name="otra_vista"),
    path('acercademi/', acercademi, name="acercademi"), 
    path('regsitrar/', registrar, name='registrar'), 
    path('login/', login, name='login'),
    path('editar/', editar, name='editar'),
    path('logout/', LogoutView.as_view(template_name='indice/logout.html'), name='logout'),
]