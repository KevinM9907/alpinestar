from rest_framework import serializers
from .models import Abastecimiento, InsumoHasAbastecimiento
from insumos.serializers import CategoriaInsumoSerializer
from insumos.serializers import InsumoSerializer
from manicuristas.serializers import ManicuristaSerializer
from manicuristas.models import Manicurista
from insumos.models import Insumo, CategoriaInsumo



class InsumoHasAbastecimientoSerializer(serializers.ModelSerializer):
    
    insumo = InsumoSerializer(read_only=True)
    
    insumo_id = serializers.PrimaryKeyRelatedField(
        queryset=Insumo.objects.all(), source='insumo', write_only=True
    )
    
    class Meta:
        model = InsumoHasAbastecimiento
        fields = '__all__'

class AbastecimientoSerializer(serializers.ModelSerializer):
    
    manicurista = ManicuristaSerializer(read_only=True)
    
    manicurista_id = serializers.PrimaryKeyRelatedField(
        queryset=Manicurista.objects.all(), source='manicurista', write_only=True
    )
    
    categoria_insumo = CategoriaInsumoSerializer(read_only=True)
    
    categoria_insumo_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoriaInsumo.objects.all(), source='categoria_insumo', write_only=True
    )
    
    insumo = InsumoSerializer(read_only=True)
    
    insumo_id = serializers.PrimaryKeyRelatedField(
        queryset=Insumo.objects.all(), source='insumo', write_only=True
    )
    
    
    class Meta:
        model = Abastecimiento
        fields = '__all__'
    

        