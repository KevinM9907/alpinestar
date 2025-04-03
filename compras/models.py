from django.db import models
from proveedores.models import Proveedor
from insumos.models import Insumo

# Create your models here.
class Compra(models.Model):
    estado = models.BooleanField()
    fecha_compra = models.DateField()
    total = models.FloatField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class CompraHasInsumo(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()
