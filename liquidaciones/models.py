from django.db import models
from manicuristas.models import Manicurista
from semanas.models import Semana

# Create your models here.
class Liquidacion(models.Model):
    valor = models.IntegerField()
    manicurista = models.ForeignKey(Manicurista, on_delete=models.CASCADE)
    bonificacion = models.IntegerField()
    semana = models.ForeignKey(Semana, on_delete=models.CASCADE)
