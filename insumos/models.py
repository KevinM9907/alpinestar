from django.db import models

# Create your models here.
class Insumo(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    estado = models.BooleanField()
    categoria = models.ForeignKey('CategoriaInsumo', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class CategoriaInsumo(models.Model):
    nombre = models.CharField(max_length=45)
    estado = models.BooleanField()
    
    
    def __str__(self):
        return self.nombre