from rest_framework import routers
from .api import LiquidacionViewSet

router = routers.DefaultRouter()

router.register('api/liquidaciones', LiquidacionViewSet, 'liquidaciones')

urlpatterns  = router.urls
