from rest_framework import serializers
from .models import Usuario, Rol, Permiso, RolHasPermiso


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

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'


class RolHasPermisoSerializer(serializers.ModelSerializer):
    
    # Mostrar detalles del rol en GET
    rol = RolSerializer(read_only=True) 
    
    # Mostrar detalles del permiso en GET
    permiso = PermisoSerializer(read_only=True)
      
    # Permite enviar solo el ID en POST y PUT
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(), source="rol", write_only=True
    )
    
    # Permite enviar solo el ID en POST y PUT
    permiso_id = serializers.PrimaryKeyRelatedField(
        queryset=Permiso.objects.all(), source="permiso", write_only=True
    )  

    class Meta:
        model = RolHasPermiso
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    
    # Mostrar información del rol en GET
    rol = RolSerializer(read_only=True)  
    
    # Para que en POST se pase solo el ID del rol
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(), source="rol", write_only=True
    )  

    class Meta:
        model = Usuario
        fields = '__all__'
        