from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('acerca_de/', acerca_de, name='acerca_de'),

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

    #___________________medicamentos
    path('medicamentos/', MedicamentoList.as_view(), name='medicamentos'),
    path('medicamento_create/', MedicamentoCreate.as_view(), name='medicamento_create'),
    path('medicamento_update/<int:pk>', MedicamentoUpdate.as_view(), name='medicamento_update'),
    path('medicamento_delete/<int:pk>', MedicamentoDelete.as_view(), name='medicamento_delete'),

    #Rutas de búsqueda
    path('buscar/', buscar, name='buscar'),  
    path('buscar_productos/', buscarProductos, name='buscar_productos'),

    #----------------------------------- login, logout y registro
    path('login/', login_request, name='login'),
    path('register/', register, name='registro'),
    # path('logout/', LogoutView.as_view(template_name="admin/logout.html"), name='logout'),
    path('logout/', logout_sesion, name='logout'),

    
    #----------------------------------- editar perfil
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),




]