from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MascotaForms(forms.Form):
    tipo=forms.ChoiceField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')])
    raza=forms.CharField(max_length=50, required=True)
    nombre=forms.CharField(max_length=50, required=True)
    edad=forms.IntegerField(required=True)

class ProductoForms(forms.Form):
    nombre_producto=forms.CharField(max_length=50, required=True)
    categoria=forms.CharField(max_length=50, required=True)
    tipo_de_animal=forms.ChoiceField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')])
    disponibilidad=forms.BooleanField(required=False)

class MedicamentoForms(forms.Form):
    nombre_medicamento = forms.CharField(max_length=50)
    descripcion = forms.Textarea()
    tipo_de_animal = forms.ChoiceField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')])
    disponibilidad= forms.BooleanField(required=False)


class RegistroForm(UserCreationForm):
    email=forms.EmailField(max_length=50, required=True)
    password1=forms.CharField(label='Contraseña', max_length=50, required=True, widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña', max_length=50, required=True,widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class UserEditForm(UserCreationForm):
    email=forms.EmailField(max_length=50, required=True)
    password1=forms.CharField(label='Contraseña', max_length=50, required=True, widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contraseña', max_length=50, required=True,widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre',max_length=50, required=True)
    last_name=forms.CharField(label='Apellido',max_length=50, required=True)
    
    class Meta:
        model=User
        fields=['email','password1','password2','first_name','last_name']
        

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)