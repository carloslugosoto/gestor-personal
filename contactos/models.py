from django.db import models
from datetime import date

# Create your models here.

class Grupo(models.Model):
    nombre = models.TextField(15)
    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    celular =  models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()
    compañia = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(default=date.today)
    nota = models.TextField(blank=True, null=True)
        
    grupo = models.ForeignKey(Grupo, on_delete= models.CASCADE, default= 1)

    def __str__(self):
        return self.nombre

