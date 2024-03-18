from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClienteForms(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    apellido=forms.CharField(max_length=50, required=True)
    mascota=forms.ChoiceField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')])
    telefono=forms.IntegerField( required=True)
    email=forms.EmailField(required=True)
    fecha_ult_compra=forms.DateField(required=False)
