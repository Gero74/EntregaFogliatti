from django.db import models

# Create your models here.
class Tematica(models.Model):
    nombre_tema=models.CharField(max_length=40)
    autor=models.CharField(max_length=40)
    codigo=models.CharField(max_length=40)
    
class Contacto(models.Model):
    nombre=models.CharField(max_length=40)
    correo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=300)


class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    correo=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=50)