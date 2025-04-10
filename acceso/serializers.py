from rest_framework import serializers
from .models import Usuario

class AccesoSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contraseña = serializers.CharField(write_only=True)

    def validate(self, data):
        correo = data.get("correo")
        contraseña = data.get("contraseña")

        try:
            usuario = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado.")

        if not usuario.check_password(contraseña):
            raise serializers.ValidationError("Contraseña incorrecta.")

        data["usuario"] = usuario
        return data
