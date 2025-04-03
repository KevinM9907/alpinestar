from rest_framework import serializers
from .models import Manicurista

class ManicuristaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Manicurista
        fields = '__all__'