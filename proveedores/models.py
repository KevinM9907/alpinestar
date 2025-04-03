from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    nit = models.CharField(max_length=10)
    direccion = models.CharField(max_length=45)
    correo = models.EmailField(max_length=45)
    estado = models.BooleanField()
    tipo_persona = models.CharField(max_length=45)
    celular =  models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.nombre