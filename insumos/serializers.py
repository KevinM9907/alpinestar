from rest_framework import serializers
from .models import Insumo, CategoriaInsumo

class CategoriaInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaInsumo
        fields = '__all__'

class InsumoSerializer(serializers.ModelSerializer):
    
    # Solo lectura en GET
    categoria_insumo = CategoriaInsumoSerializer(read_only=True)  
    
    # Para POST y PUT
    categoria_insumo_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoriaInsumo.objects.all(), source="categoria_insumo", write_only=True)  
    
    class Meta: 
        model = Insumo
        fields = '__all__'