from rest_framework import routers
from .api import NovedadViewSet

router = routers.DefaultRouter()

router.register('api/novedades', NovedadViewSet, 'novedades')

urlpatterns  = router.urls