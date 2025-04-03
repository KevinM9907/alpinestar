from rest_framework import serializers
from .models import Liquidacion
from semanas.serializers import SemanaSerializer

class LiquidacionSerializer(serializers.ModelSerializer):
    
    # Solo lectura en GET
    semanas = SemanaSerializer(read_only=True)
    
    # Para POST y PUT
    semanas_id = serializers.PrimaryKeyRelatedField(
        queryset=SemanaSerializer.Meta.model.objects.all(), source="semanas", write_only=True
    )  
    
    class Meta:
        model = Liquidacion
        fields = '__all__'