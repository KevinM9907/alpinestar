from rest_framework import serializers
from .models import Cita
from clientes.serializers import ClienteSerializer
from manicuristas.serializers import ManicuristaSerializer
from servicios.serializers import ServicioSerializer


class CitaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    manicurista = ManicuristaSerializer()
    servicio = ServicioSerializer()
    
    class Meta:
        model = Cita
        fields = '__all__'