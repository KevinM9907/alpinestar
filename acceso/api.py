from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import AccesoSerializer

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AccesoSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.validated_data["usuario"]
            # Aquí puedes devolver un token o los datos del usuario
            return Response({
                "mensaje": "Login exitoso",
                "usuario_id": usuario.id,
                "correo": usuario.correo,
                # Aquí podrías incluir un token JWT si usas uno
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
