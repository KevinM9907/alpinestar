from rest_framework import routers
from .api import ServicioViewSet

router = routers.DefaultRouter()

router.register('api/servicios', ServicioViewSet, 'servicios')

urlpatterns  = router.urls