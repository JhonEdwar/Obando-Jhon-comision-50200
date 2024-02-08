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

def mascotasForm(request):
    mascotaForm=MascotaForms()
    return render(request,'apptienda/mascotasForm.html',{'mascota_form':mascotaForm})
