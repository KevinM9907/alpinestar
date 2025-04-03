from .models import Liquidacion
from rest_framework import viewsets, permissions
from .serializers import LiquidacionSerializer

class LiquidacionViewSet(viewsets.ModelViewSet):
    queryset = Liquidacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LiquidacionSerializer