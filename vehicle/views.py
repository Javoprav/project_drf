from rest_framework import viewsets, generics

from vehicle.models import Motorcycle
from vehicle.serializers import MotorcycleSerializers


class MotorcycleViewSet(viewsets.ModelViewSet):
    serializer_class = MotorcycleSerializers
    queryset = Motorcycle.objects.all()
    