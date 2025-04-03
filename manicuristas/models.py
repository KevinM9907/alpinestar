from django.db import models

# Create your models here.
class Manicurista(models.Model):
    nombres = models.CharField(max_length=45) 
    apellidos = models.CharField(max_length=45)
    estado = models.BooleanField()