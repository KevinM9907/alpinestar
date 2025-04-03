from .models import Abastecimiento
from rest_framework import viewsets, permissions
from .serializers import AbastecimientoSerializer

class AbastecimientoViewSet(viewsets.ModelViewSet):
    queryset = Abastecimiento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AbastecimientoSerializer