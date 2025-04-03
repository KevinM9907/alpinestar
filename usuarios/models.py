from django.db import models

# Create your models here.
class Usuario(models.Model):
    celular = models.CharField(max_length=10)
    correo = models.EmailField(max_length=45)
    contrasena = models.CharField(max_length=45)
    estado = models.BooleanField()
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)


class Rol(models.Model):
    nombre = models.CharField(max_length=45)
    estado = models.BooleanField()

class Permiso(models.Model):
    nombre = models.CharField(max_length=45)
    estado = models.BooleanField()
    
class RolHasPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)