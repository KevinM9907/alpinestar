from django.db import models

# Create your models here.
class Cliente(models.Model):
    tipo_documento = models.CharField(max_length=45)
    num_documento = models.CharField(max_length=10)
    nombres = models.CharField(max_length=45)
    correo = models.EmailField(max_length=45)
    celular = models.CharField(max_length=10)