from django import forms

class MascotaForms(forms.Form):
    tipo=forms.CharField(max_length=50, required=True)
    raza=forms.CharField(max_length=50, required=True)
    nombre=forms.CharField(max_length=50, required=True)
    edad=forms.IntegerField(required=True)
