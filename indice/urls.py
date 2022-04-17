from django.urls import path
from .views import inicio, pages, pagesid, otra_vista, acercademi, login, registrar, editar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('pages/', pages, name="pages"),
    path('pages/<id>', pagesid, name="leer_mas"),
    path('otra-vista/', otra_vista, name="otra_vista"),
    path('about/', acercademi, name="about"), 
    path('regsitrar/', registrar, name='registrar'), 
    path('login/', login, name='login'),
    path('editar/', editar, name='editar'),
    path('logout/', LogoutView.as_view(template_name='indice/logout.html'), name='logout'),
]