from rest_framework import serializers
from .models import Abastecimiento, InsumoHasAbastecimiento
from insumos.serializers import InsumoSerializer
from manicuristas.serializers import ManicuristaSerializer

class InsumoHasAbastecimientoSerializer(serializers.ModelSerializer):
    insumo = InsumoSerializer()
    
    class Meta:
        model = InsumoHasAbastecimiento
        fields = '__all__'

class AbastecimientoSerializer(serializers.ModelSerializer):
    manicurista = ManicuristaSerializer()
    
    # Usa esta relación inversa para obtener los insumos relacionados con el abastecimiento.
    insumos = InsumoHasAbastecimientoSerializer(many=True, source='insumo_has_abastecimiento_set')
    
    class Meta:
        model = Abastecimiento
        fields = '__all__'
    

        