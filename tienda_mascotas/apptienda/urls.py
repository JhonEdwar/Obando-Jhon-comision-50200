from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('clientes/', clientes, name='clientes'),
    path('mascotas/', mascotas, name='mascotas'),
    path('productos/', productos, name='productos'),
    #Rutas de formulario
    path('clientes_form/', clientesForm, name='clientes_form'),
    path('mascotas_form/', mascotasForm, name='curso_form'),
    path('productos_form/', productosForm, name='productos_form'),
    #Rutas de búsqueda
    path('buscar/', buscar, name='buscar'),  
    path('buscar_productos/', buscarProductos, name='buscar_productos'),

]