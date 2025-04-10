from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AccesoSerializer, UsuarioSerializer, RegistroSerializer
from .models import Usuario

class AuthBaseView(APIView):
    """Clase base para vistas de autenticación"""
    permission_classes = [permissions.AllowAny]

class LoginView(AuthBaseView):
    def post(self, request):
        serializer = AccesoSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {
                    'error': 'Error de validación',
                    'detalles': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        usuario = serializer.validated_data['usuario']
        refresh = RefreshToken.for_user(usuario)
        
        return Response({
            'mensaje': 'Login exitoso',
            'usuario': {
                'id': usuario.id,
                'correo': usuario.correo,
                'rol': usuario.rol.nombre,
            },
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_200_OK)

class RegistroView(AuthBaseView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {
                    'error': 'Error en el registro',
                    'detalles': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        usuario = serializer.save()
        
        # Opcional: generar token automáticamente después del registro
        refresh = RefreshToken.for_user(usuario)
        
        return Response({
            'mensaje': 'Usuario registrado exitosamente',
            'usuario': {
                'id': usuario.id,
                'correo': usuario.correo,
                'rol': usuario.rol.nombre,
            },
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_201_CREATED)

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.none()  # Por defecto vacío, se sobrescribe en get_queryset

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_superuser:
            return Usuario.objects.all()
        elif user.is_authenticated:
            return Usuario.objects.filter(id=user.id)
        return Usuario.objects.none()

    def perform_create(self, serializer):
        # Hashear la contraseña al crear el usuario
        usuario = serializer.save()
        if 'password' in serializer.validated_data:
            usuario.set_password(serializer.validated_data['password'])
            usuario.save()

    def perform_update(self, serializer):
        # Hashear la contraseña si se actualiza
        usuario = serializer.save()
        if 'password' in serializer.validated_data:
            usuario.set_password(serializer.validated_data['password'])
            usuario.save()