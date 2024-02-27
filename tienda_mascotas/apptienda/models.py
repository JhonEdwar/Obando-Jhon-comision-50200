from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    mascota= models.CharField(max_length=50)
    telefono=models.IntegerField()
    email = models.EmailField()
    fecha_ult_compra = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Mascota(models.Model):
    tipo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    edad= models.IntegerField()

    def __str__(self):
        return f"{self.tipo} de nombre {self.nombre}"

   
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    tipo_de_animal = models.CharField(max_length=50)
    disponibilidad= models.BooleanField()

    def __str__(self):
        return f"{self.nombre_producto}"
    