from .models import Manicurista
from rest_framework import viewsets, permissions
from .serializers import ManicuristaSerializer

class ManicuristaViewSet(viewsets.ModelViewSet):
    queryset = Manicurista.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ManicuristaSerializer