from .models import Compra
from rest_framework import viewsets, permissions
from .serializers import CompraSerializers

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CompraSerializers