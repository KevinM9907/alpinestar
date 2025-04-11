from django.urls import path
from rest_framework import routers
from .api import LoginView, UsuarioViewSet, RegistroView

router = routers.DefaultRouter()

router.register('api/usuarios', UsuarioViewSet, 'usuarios')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
     path('registro/', RegistroView.as_view(), name='registro'),
] + router.urls