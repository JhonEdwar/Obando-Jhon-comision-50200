from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    mascota= models.CharField(max_length=50)
    telefono=models.IntegerField()
    email = models.EmailField()
    ultima_compra = models.DateField()

class Mascota(models.Model):
    tipo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    edad= models.IntegerField()
   
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    tipo_de_animal = models.CharField(max_length=50)
    disponibilidad= models.BooleanField()
    