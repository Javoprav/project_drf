from rest_framework.routers import DefaultRouter

from vehicle.views import MotorcycleViewSet

router = DefaultRouter()
router.register(r'moto', MotorcycleViewSet, basename='moto')


urlpatterns = [] + router.urls
