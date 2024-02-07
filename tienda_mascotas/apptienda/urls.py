from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('clientes/', clientes, name='clientes'),
    path('mascotas/', mascotas, name='mascotas'),
    path('productos/', productos, name='productos'),

]