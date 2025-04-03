from django.db import models
from manicuristas.models import Manicurista
from insumos.models import Insumo

# Create your models here.
class Abastecimiento(models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField()
    manicurista = models.ForeignKey(Manicurista, on_delete=models.CASCADE)

class InsumoHasAbastecimiento(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    abastecimiento = models.ForeignKey(Abastecimiento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()