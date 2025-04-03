from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.FloatField()
    descripcion = models.TextField()
    estado = models.BooleanField()
    
class VentaServicio(models.Model):
    fecha = models.DateField()
    precio = models.FloatField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)