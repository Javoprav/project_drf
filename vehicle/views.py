from rest_framework import viewsets, generics

from vehicle.models import Motorcycle, Car, Milage
from vehicle.serializers import MotorcycleSerializers, CarSerializers, MilageSerializer, MotoMilageSerializer


class MotorcycleViewSet(viewsets.ModelViewSet):
    serializer_class = MotorcycleSerializers
    queryset = Motorcycle.objects.all()


class CarRetrieveView(generics.RetrieveAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()


class CarListView(generics.ListAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()


class CarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CarSerializers


class CarDestroyView(generics.DestroyAPIView):
    queryset = Car.objects.all()


class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarSerializers


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


class MilageMotoListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer
