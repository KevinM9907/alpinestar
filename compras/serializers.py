from rest_framework import serializers
from .models import Compra, CompraHasInsumo
from insumos.serializers import InsumoSerializer
from proveedores.serializers import ProveedorSerializer
from proveedores.models import Proveedor

class CompraSerializers(serializers.ModelSerializer):
    
    # Mostrar información completa en GET
    proveedor = ProveedorSerializer(read_only=True) 
    
    # Permite enviar solo el ID en POST y PUT
    proveedor_id = serializers.PrimaryKeyRelatedField(
        queryset=Proveedor.objects.all(), source="proveedor", write_only=True
    )  
    
    class Meta:
        model = Compra
        fields = '__all__'

class CompraHasInsumoSerializer(serializers.ModelSerializer):
    
    # Mostrar detalles del insumo en GET
    insumo = InsumoSerializer(read_only=True)  
    
    # Permite enviar solo el ID en POST y PUT
    insumo_id = serializers.PrimaryKeyRelatedField(
        queryset=InsumoSerializer.Meta.model.objects.all(), source="insumo", write_only=True
    )  

    
    class Meta:
        model = CompraHasInsumo
        fields = '__all__'
