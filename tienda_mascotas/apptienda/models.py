from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    mascota=models.CharField(max_length=20, choices=[
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]) 
    telefono=models.IntegerField()
    email = models.EmailField()
    fecha_ult_compra = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Mascota(models.Model):
    tipo = models.CharField(max_length=20, choices=[
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]) 
    raza = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    edad= models.IntegerField()

    def __str__(self):
        return f"{self.tipo} de nombre {self.nombre}"

   
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    tipo_de_animal =models.CharField(max_length=20, choices=[
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]) 
    disponibilidad= models.BooleanField()

    def __str__(self):
        return f"{self.nombre_producto}"
    

class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    tipo_de_animal = models.CharField(max_length=20, choices=[
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ])    
    disponibilidad= models.BooleanField()

    def __str__(self):
        return f"{self.nombre_medicamento}"
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_producto} {self.imagen}"
    
