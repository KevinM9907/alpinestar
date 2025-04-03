from rest_framework import routers
from .api import ManicuristaViewSet

router = routers.DefaultRouter()

router.register('api/manicuristas', ManicuristaViewSet, 'manicuristas')

urlpatterns  = router.urls