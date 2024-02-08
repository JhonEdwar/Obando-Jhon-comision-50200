from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request,'apptienda/home.html')

def clientes(request):
    contexto={'clientes': Cliente.objects.all()}
    return render(request,'apptienda/clientes.html',contexto)

def mascotas(request):
    contexto={'mascotas':Mascota.objects.all()}
    return render(request,'apptienda/mascotas.html',contexto)

def productos(request):
    contexto={'productos':Producto.objects.all()}
    return render(request,'apptienda/productos.html',contexto)


def clientesForm(request):
    if request.method == 'POST':
        clienteForm= ClienteForms(request.POST)
        if clienteForm.is_valid():
            cliente_nombre=clienteForm.cleaned_data.get('nombre')
            cliente_apellido=clienteForm.cleaned_data.get('apellido')
            cliente_mascota=clienteForm.cleaned_data.get('mascota')
            cliente_telefono=clienteForm.cleaned_data.get('telefono')
            cliente_email=clienteForm.cleaned_data.get('email')
            cliente_compra=clienteForm.cleaned_data.get('ultima_compra')
            ClienteSave=Cliente(nombre=cliente_nombre,apellido=cliente_apellido,mascota=cliente_mascota,telefono=cliente_telefono,email=cliente_email,ultima_compra=cliente_compra)
            ClienteSave.save()
            return render(request,'apptienda/home.html')
    else:
        clienteForm= ClienteForms()

    return render(request,'apptienda/clientesForm.html',{'cliente_form':clienteForm})




def mascotasForm(request):
    if request.method == 'POST':
        mascotaForm= MascotaForms(request.POST)
        if mascotaForm.is_valid():
            mascota_tipo=mascotaForm.cleaned_data.get('tipo')
            mascota_raza=mascotaForm.cleaned_data.get('raza')
            mascota_nombre=mascotaForm.cleaned_data.get('nombre')
            mascota_edad=mascotaForm.cleaned_data.get('edad')
            mascotasave=Mascota(tipo=mascota_tipo,raza=mascota_raza,nombre=mascota_nombre,edad=mascota_edad)
            mascotasave.save()
            return render(request,'apptienda/home.html')
    else:
        mascotaForm=MascotaForms()

    return render(request,'apptienda/mascotasForm.html',{'mascota_form':mascotaForm})


def productosForm(request):
    if request.method == 'POST':
        productoForm= ProductoForms(request.POST)
        if productoForm.is_valid():
            producto_nombre=productoForm.cleaned_data.get('nombre_producto')
            producto_categoria=productoForm.cleaned_data.get('categoria')
            producto_animal=productoForm.cleaned_data.get('tipo_de_animal')
            producto_disponibilidad=productoForm.cleaned_data.get('disponibilidad')
            productoSave=Producto(nombre_producto=producto_nombre,categoria=producto_categoria,tipo_de_animal=producto_animal,disponibilidad=producto_disponibilidad)
            productoSave.save()
            return render(request,'apptienda/home.html')
    else:
        productoForm= ProductoForms()

    return render(request,'apptienda/productosForm.html',{'producto_form':productoForm})