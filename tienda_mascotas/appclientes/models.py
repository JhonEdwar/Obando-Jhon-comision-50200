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

