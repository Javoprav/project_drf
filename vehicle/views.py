from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from vehicle.models import Motorcycle, Car, Milage
from vehicle.permissions import OwnerOrStuff
from vehicle.serializers import MotorcycleSerializers, CarSerializers, MilageSerializer, MotoMilageSerializer, \
    CarCreateSerializers


class MotorcycleViewSet(viewsets.ModelViewSet):
    serializer_class = MotorcycleSerializers
    queryset = Motorcycle.objects.all()


class CarRetrieveView(generics.RetrieveAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()


class CarListView(generics.ListAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]


class CarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CarSerializers


class CarRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
    permission_classes = [OwnerOrStuff]


class CarDestroyView(generics.DestroyAPIView):
    queryset = Car.objects.all()


class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarCreateSerializers


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


class MilageMotoListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer


"""Реализовать эндпоинт для получения пробегов и добавить фильтрацию:
выводить список только пробегов для машин,
выводить список только пробегов для мотоциклов,
изменять последовательность сортировки по году пробега.
Шаги решения
Установить пакет django-filter.
Описать класс фильтр для фильтрации данных.
Описать атрибуты для контроллера для изменения порядка сортировки.
Вспомогательный материал: https://www.django-rest-framework.org/api-guide/filtering/#api-guide"""


class MilageListAPIView(generics.ListAPIView):

    queryset = Milage.objects.all()
    serializer_class = MilageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['car', 'moto']
    ordering_fields = ['year']
