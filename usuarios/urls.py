from django.urls import path
from rest_framework import routers
from .api import LoginView, UsuarioViewSet

router = routers.DefaultRouter()

router.register('api/usuarios', UsuarioViewSet, 'usuarios')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
] + router.urls