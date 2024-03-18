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



#_______________________________-clientes


class ClientesList(ListView):
    model=Cliente
    
class ClientesCreate(CreateView):
    model=Cliente
    fields=['nombre','apellido','mascota','telefono','email','fecha_ult_compra']
    success_url=reverse_lazy('clientes')

class ClientesUpdate(UpdateView):
    model=Cliente
    fields=['nombre','apellido','mascota','telefono','email','fecha_ult_compra']
    success_url=reverse_lazy('clientes')

class ClientesDelete(DeleteView):
    model=Cliente
    success_url=reverse_lazy('clientes')
