from rest_framework.routers import DefaultRouter
from django.urls import path
from vehicle.views import *

router = DefaultRouter()
router.register(r'moto', MotorcycleViewSet, basename='moto')


urlpatterns = [
    # Cars
    path('car/', CarListView.as_view(), name='car_list'),
    path('car_list/', Car_ListView.as_view(), name='car__list'),
    path('car/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto_create'),
    path('car/<int:pk>/', CarRetrieveAPIView.as_view(), name='car_view'),
    path('car/set_like/', SetLikeToCar.as_view(), name='set_like'),

    # Milage
    path('car/milage/<int:pk>/', CarMilageCreateAPIView.as_view(), name='car_milage_create'),
    path('moto/milage/<int:pk>/', MotoMilageCreateAPIView.as_view(), name='moto_milage_create'),
    path('milage/', MilageListAPIView.as_view(), name='milage_list'),
    path('milage/create/', MilageCreateAPIView.as_view(), name='milage_create'),
    path('milage/moto/', MilageMotoListAPIView.as_view(), name='milage_moto_list'),

    path('total/', TotalAPIView.as_view(), name='total'),
] + router.urls
