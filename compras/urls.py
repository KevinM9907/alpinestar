from rest_framework import routers
from .api import CompraViewSet

router = routers.DefaultRouter()

router.register('api/compras', CompraViewSet, 'compras')

urlpatterns  = router.urls