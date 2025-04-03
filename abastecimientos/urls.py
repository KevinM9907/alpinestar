from rest_framework import routers
from .api import AbastecimientoViewSet

router = routers.DefaultRouter()

router.register('api/abastecimiento', AbastecimientoViewSet, 'abastecimiento')

urlpatterns = router.urls
