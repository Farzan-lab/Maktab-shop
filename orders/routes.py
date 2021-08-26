from rest_framework.routers import DefaultRouter
from .api import OrderViewSet


router = DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = router.urls