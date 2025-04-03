from rest_framework import routers
from .api import SemanaViewSet

router = routers.DefaultRouter()

router.register('api/semanas', SemanaViewSet, 'semanas')

urlpatterns  = router.urls