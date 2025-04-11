from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Usuario, Rol, Permiso, RolHasPermiso

class AccesoSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contraseña = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        correo = data.get('correo')
        contraseña = data.get('contraseña')

        if correo and contraseña:
            usuario = authenticate(
                request=self.context.get('request'),
                username=correo,
                password=contraseña
            )
            
            if not usuario:
                raise serializers.ValidationError("Credenciales inválidas")
                
            if not usuario.is_active:
                raise serializers.ValidationError("Cuenta inactiva")
                
            data['usuario'] = usuario
            return data
            
        raise serializers.ValidationError("Debe ingresar correo y contraseña")

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
        