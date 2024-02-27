from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClienteForms(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    apellido=forms.CharField(max_length=50, required=True)
    mascota=forms.CharField(max_length=50, required=True)
    telefono=forms.IntegerField( required=True)
    email=forms.EmailField(required=True)
    fecha_ult_compra=forms.DateField(required=False)

class MascotaForms(forms.Form):
    tipo=forms.CharField(max_length=50, required=True)
    raza=forms.CharField(max_length=50, required=True)
    nombre=forms.CharField(max_length=50, required=True)
    edad=forms.IntegerField(required=True)

class ProductoForms(forms.Form):
    nombre_producto=forms.CharField(max_length=50, required=True)
    categoria=forms.CharField(max_length=50, required=True)
    tipo_de_animal=forms.CharField(max_length=50, required=True)
    disponibilidad=forms.BooleanField(required=False)


class RegistroForm(UserCreationForm):
    email=forms.EmailField(max_length=50, required=True)
    password1=forms.CharField(label='Contraseña', max_length=50, required=True, widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña', max_length=50, required=True,widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']