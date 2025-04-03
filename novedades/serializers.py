from rest_framework import serializers
from .models import Novedad
from manicuristas.serializers import ManicuristaSerializer
from manicuristas.models import Manicurista

class NovedadSerializer(serializers.ModelSerializer):
    
    # Solo lectura en GET
    manicuristas = ManicuristaSerializer(read_only=True)
    
    
    class Meta:
        model = Novedad
        fields = '__all__'