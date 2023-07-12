from rest_framework.routers import DefaultRouter
from django.urls import path
from vehicle.views import MotorcycleViewSet, CarListView, CarCreateAPIView, MilageCreateAPIView, MilageMotoListAPIView, \
    MilageListAPIView, CarRetrieveAPIView

router = DefaultRouter()
router.register(r'moto', MotorcycleViewSet, basename='moto')


urlpatterns = [
    # Cars
    path('car/', CarListView.as_view(), name='car_list'),
    path('car/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('car/<int:pk>/', CarRetrieveAPIView.as_view(), name='car_view'),

    # Milage
    path('milage/', MilageListAPIView.as_view(), name='milage_list'),
    path('milage/create/', MilageCreateAPIView.as_view(), name='milage_create'),
    path('milage/moto/', MilageMotoListAPIView.as_view(), name='milage_moto_list'),
] + router.urls
