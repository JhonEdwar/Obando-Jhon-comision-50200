from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# home
def home(request):
    return render(request,'apptienda/home.html')


#_______________________________-clientes


class ClientesList(LoginRequiredMixin,ListView):
    model=Cliente
    
class ClientesCreate(LoginRequiredMixin,CreateView):
    model=Cliente
    fields=['nombre','apellido','mascota','telefono','email','fecha_ult_compra']
    success_url=reverse_lazy('clientes')

class ClientesUpdate(LoginRequiredMixin,UpdateView):
    model=Cliente
    fields=['nombre','apellido','mascota','telefono','email','fecha_ult_compra']
    success_url=reverse_lazy('clientes')

class ClientesDelete(LoginRequiredMixin,DeleteView):
    model=Cliente
    success_url=reverse_lazy('clientes')


# -------------------------sección productos

class ProductosList(LoginRequiredMixin,ListView):
    model=Producto
    
class ProductosCreate(LoginRequiredMixin,CreateView):
    model=Producto
    fields=['nombre_producto','categoria','tipo_de_animal','disponibilidad']
    success_url=reverse_lazy('productos')

class ProductosUpdate(LoginRequiredMixin,UpdateView):
    model=Producto
    fields=['nombre_producto','categoria','tipo_de_animal','disponibilidad']
    success_url=reverse_lazy('productos')

class ProductosDelete(LoginRequiredMixin,DeleteView):
    model=Producto
    success_url=reverse_lazy('productos')

# -------------------------sección mascotas

class MascotasList(LoginRequiredMixin,ListView):
    model=Mascota
    
class MascotasCreate(LoginRequiredMixin,CreateView):
    model=Mascota
    fields=['tipo','raza','nombre','edad']
    success_url=reverse_lazy('mascotas')

class MascotasUpdate(LoginRequiredMixin,UpdateView):
    model=Mascota
    fields=['tipo','raza','nombre','edad']
    success_url=reverse_lazy('mascotas')

class MascotasDelete(LoginRequiredMixin,DeleteView):
    model=Mascota
    success_url=reverse_lazy('mascotas')


# -------------------------sección búsqueda
@login_required
def buscar(request):
    return render(request,'apptienda/buscar.html')

@login_required
def buscarProductos(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        productos=Producto.objects.filter(nombre_producto__icontains=patron)
        contexto={'productos':productos}
        return render(request,'apptienda/productos.html',contexto)
    else:
        return HttpResponse('no se ingresaron patrones de búsqueda')
    

#----------------------------------- login, logout y registro
    
    
def login_request(request):
    if request.method == 'POST':
        usuario=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=usuario, password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm= AuthenticationForm()
    return render(request,'apptienda/login.html',{'form':miForm})


def register(request):
    if request.method == 'POST':
        miForm= RegistroForm(request.POST)
        if miForm.is_valid():
            usuario=miForm.cleaned_data.get('username')
            # password=miForm.cleaned_data.get('password')
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm= RegistroForm()
    return render(request,'apptienda/registro.html',{'form':miForm})