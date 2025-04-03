from django.db import models
from manicuristas.models import Manicurista

# Create your models here.
class Novedad(models.Model):
    hora_entrada = models.DateTimeField()
    hora_salida = models.DateTimeField()
    motivo = models.CharField(max_length=50)
    estado = models.BooleanField()
    manicurista = models.ForeignKey(Manicurista, on_delete=models.CASCADE)