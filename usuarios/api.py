from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework_simplejwt.tokens import RefreshToken  # Nuevo: Para JWT
from .serializers import AccesoSerializer, UsuarioSerializer
from .models import Usuario

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Mantener acceso público solo para login

    def post(self, request):
        serializer = AccesoSerializer(data=request.data, context={'request': request})  # Mejorado
        if serializer.is_valid():
            usuario = serializer.validated_data["usuario"]
            
            # Opción 1: Respuesta básica (como tenías originalmente)
            response_data = {
                "mensaje": "Login exitoso",
                "usuario_id": usuario.id,
                "correo": usuario.correo,
                "rol": usuario.rol.nombre if usuario.rol else None  # Nuevo: info de rol
            }

            # Opción 2: Con JWT (recomendado para producción) - Descomenta si lo implementas
            refresh = RefreshToken.for_user(usuario)
            response_data['tokens'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsuarioSerializer