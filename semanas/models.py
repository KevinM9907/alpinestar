from django.db import models

# Create your models here.
class Semana(models.Model):
    numero_semana = models.CharField(max_length=45)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()