from rest_framework import serializers
from .models import Servicio, VentaServicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
        
class VentaServicioSerializer(serializers.ModelSerializer):
    
    
    servicio = ServicioSerializer() 
     
    class Meta:
        model = VentaServicio
        fields = '__all__'