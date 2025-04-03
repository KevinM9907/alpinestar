from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.FloatField()
    descripcion = models.TextField()
    estado = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
class VentaServicio(models.Model):
    fecha = models.DateField()
    precio = models.FloatField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)