from .models import Cita
from rest_framework import viewsets, permissions
from .serializers import CitaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CitaSerializer