from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario, Rol, Permiso, RolHasPermiso

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'
        read_only_fields = ['id']

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        read_only_fields = ['id']

class RolHasPermisoSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)
    permiso = PermisoSerializer(read_only=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(), 
        source='rol', 
        write_only=True
    )
    permiso_id = serializers.PrimaryKeyRelatedField(
        queryset=Permiso.objects.all(), 
        source='permiso', 
        write_only=True
    )

    class Meta:
        model = RolHasPermiso
        fields = ['id', 'rol', 'permiso', 'rol_id', 'permiso_id']
        read_only_fields = ['id']

class UsuarioBaseSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'correo', 'celular', 'password', 'estado', 'rol']
        extra_kwargs = {
            'password': {'write_only': True},
            'correo': {'required': True}
        }

class AccesoSerializer(serializers.Serializer):
    correo = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        correo = data.get('correo')
        password = data.get('password')
        
        if not (correo and password):
            raise serializers.ValidationError("Correo y contraseña son requeridos")
            
        usuario = Usuario.objects.filter(correo=correo).first()
        
        if not usuario:
            raise serializers.ValidationError("Credenciales inválidas")
            
        if not usuario.check_password(password):
            raise serializers.ValidationError("Credenciales inválidas")
            
        if not usuario.estado:
            raise serializers.ValidationError("Cuenta inactiva")
            
        data['usuario'] = usuario
        return data

class RegistroSerializer(UsuarioBaseSerializer):
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        source='rol',
        write_only=True,
        required=True
    )

    def validate_correo(self, value):
        value = value.lower().strip()
        if Usuario.objects.filter(correo=value).exists():
            raise serializers.ValidationError("El correo ya está registrado")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta(UsuarioBaseSerializer.Meta):
        fields = UsuarioBaseSerializer.Meta.fields + ['rol_id']

class UsuarioSerializer(UsuarioBaseSerializer):
    rol = RolSerializer(read_only=True)
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset=Rol.objects.all(),
        source='rol',
        write_only=True
    )

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

    class Meta(UsuarioBaseSerializer.Meta):
        fields = UsuarioBaseSerializer.Meta.fields + ['rol', 'rol_id']