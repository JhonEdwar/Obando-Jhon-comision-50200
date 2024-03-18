from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [

    #____________________clientes

    path('', ClientesList.as_view(), name='clientes'),
    path('clientes_create/', ClientesCreate.as_view(), name='cliente_create'),
    path('clientes_update/<int:pk>', ClientesUpdate.as_view(), name='cliente_update'),
    path('clientes_delete/<int:pk>', ClientesDelete.as_view(), name='cliente_delete'),
  

]