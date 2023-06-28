from rest_framework import viewsets, generics

from vehicle.models import Motorcycle, Car
from vehicle.serializers import MotorcycleSerializers, CarSerializers


class MotorcycleViewSet(viewsets.ModelViewSet):
    serializer_class = MotorcycleSerializers
    queryset = Motorcycle.objects.all()


class CarListView(generics.ListAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()


class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarSerializers