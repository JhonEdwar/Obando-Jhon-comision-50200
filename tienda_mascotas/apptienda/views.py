from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    return render(request,'apptienda/home.html')

def clientes(request):
    contexto={'clientes': Cliente.objects.all()}
    return render(request,'apptienda/clientes.html',contexto)

def mascotas(request):
    return render(request,'apptienda/mascotas.html')

def productos(request):
    return render(request,'apptienda/productos.html')
