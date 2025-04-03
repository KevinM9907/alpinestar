from .models import Insumo
from rest_framework import viewsets, permissions
from .serializers import InsumoSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InsumoSerializer