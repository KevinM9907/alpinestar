from rest_framework import routers
from .api import CitaViewSet

router = routers.DefaultRouter()

router.register('api/citas', CitaViewSet, 'citas')

urlpatterns  = router.urls
