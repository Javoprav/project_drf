from rest_framework.routers import DefaultRouter
from django.urls import path
from vehicle.views import MotorcycleViewSet, CarListView, CarCreateAPIView, MilageCreateAPIView

router = DefaultRouter()
router.register(r'moto', MotorcycleViewSet, basename='moto')


urlpatterns = [
    # Cars
    path('car/', CarListView.as_view(), name='car_list'),
    path('car/create', CarCreateAPIView.as_view(), name='car_create'),

    # Milage
    path('milage/create', MilageCreateAPIView.as_view(), name='milage_create'),
] + router.urls
