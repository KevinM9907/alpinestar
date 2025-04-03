from .models import Novedad
from rest_framework import viewsets, permissions
from .serializers import NovedadSerializer

class NovedadViewSet(viewsets.ModelViewSet):
    queryset = Novedad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NovedadSerializer