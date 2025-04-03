from rest_framework import routers
from .api import InsumoViewSet

router = routers.DefaultRouter()

router.register('api/insumos', InsumoViewSet, 'insumos')

urlpatterns  = router.urls