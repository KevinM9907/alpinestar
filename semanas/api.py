from .models import Semana
from rest_framework import viewsets, permissions
from .serializers import SemanaSerializer

class SemanaViewSet(viewsets.ModelViewSet):
    queryset = Semana.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SemanaSerializer