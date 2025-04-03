from rest_framework import serializers
from .models import Cita
from clientes.serializers import ClienteSerializer
from manicuristas.serializers import ManicuristaSerializer
from servicios.serializers import ServicioSerializer
from clientes.models import Cliente
from manicuristas.models import Manicurista
from servicios.models import Servicio


class CitaSerializer(serializers.ModelSerializer):
    
    cliente = ClienteSerializer(read_only=True)
    
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), source='cliente', write_only=True
    )
    
    manicurista = ManicuristaSerializer(read_only=True)
    
    manicurista_id =serializers.PrimaryKeyRelatedField(
        queryset=Manicurista.objects.all(), source='manicurista', write_only=True
    )
    
    
    servicio = ServicioSerializer(read_only=True)
    
    servicio_id = serializers.PrimaryKeyRelatedField(
        queryset=Servicio.objects.all(), source='servicio', write_only=True
    )
    
    class Meta:
        model = Cita
        fields = '__all__'