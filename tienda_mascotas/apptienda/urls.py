from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home'),

    #____________________clientes

    path('clientes/', ClientesList.as_view(), name='clientes'),
    path('clientes_create/', ClientesCreate.as_view(), name='cliente_create'),
    path('clientes_update/<int:pk>', ClientesUpdate.as_view(), name='cliente_update'),
    path('clientes_delete/<int:pk>', ClientesDelete.as_view(), name='cliente_delete'),
  
    #___________________mascotas
    path('mascotas/', MascotasList.as_view(), name='mascotas'),
    path('mascotas_create/', MascotasCreate.as_view(), name='mascota_create'),
    path('mascotas_update/<int:pk>', MascotasUpdate.as_view(), name='mascota_update'),
    path('mascotas_delete/<int:pk>', MascotasDelete.as_view(), name='mascota_delete'),

    #___________________productos
    path('productos/', ProductosList.as_view(), name='productos'),
    path('producto_create/', ProductosCreate.as_view(), name='producto_create'),
    path('producto_update/<int:pk>', ProductosUpdate.as_view(), name='producto_update'),
    path('producto_delete/<int:pk>', ProductosDelete.as_view(), name='producto_delete'),

    #Rutas de búsqueda
    path('buscar/', buscar, name='buscar'),  
    path('buscar_productos/', buscarProductos, name='buscar_productos'),

    #----------------------------------- login, logout y registro
    path('login/', login_request, name='login'),
    path('register/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name="admin/logout.html"), name='logout'),

]