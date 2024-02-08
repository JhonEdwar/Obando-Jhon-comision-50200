from django import forms


class ClienteForms(forms.Form):
    apellido=forms.CharField(max_length=50, required=True)
    mascota=forms.CharField(max_length=50, required=True)
    telefono=forms.IntegerField( required=True)
    email=forms.EmailField(required=True)
    ultima_compra=forms.DateField(required=True)

class MascotaForms(forms.Form):
    tipo=forms.CharField(max_length=50, required=True)
    raza=forms.CharField(max_length=50, required=True)
    nombre=forms.CharField(max_length=50, required=True)
    edad=forms.IntegerField(required=True)

class ProductoForms(forms.Form):
    nombre_producto=forms.CharField(max_length=50, required=True)
    categoria=forms.CharField(max_length=50, required=True)
    tipo_de_animal=forms.CharField(max_length=50, required=True)
    disponibilidad=forms.BooleanField(required=True)
