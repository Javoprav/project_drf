from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from vehicle.models import Motorcycle, Car, Milage
from vehicle.pagination import MaterialsPagination, MotoPagination
from vehicle.permissions import OwnerOrStuff
from vehicle.serializers import *
from vehicle.tasks import milage_check


class MotorcycleViewSet(viewsets.ModelViewSet):
    serializer_class = MotorcycleSerializers
    queryset = Motorcycle.objects.all()
    pagination_class = MotoPagination


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotorcycleSerializers


class CarRetrieveView(generics.RetrieveAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()


class CarListView(generics.ListAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPagination  # пагинация


class Car_ListView(generics.ListAPIView):
    serializer_class = Car_Serializers
    queryset = Car.objects.all()


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

    def perform_create(self, serializer):
        self.object = serializer.save()
        milage_check.delay(self.object.pk)


class MilageMotoListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer


class MotoMilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateMilageSerializer

    def perform_create(self, serializer):
        self.object = serializer.save()
        milage_check.delay(self.object.pk)


class CarMilageCreateAPIView(generics.CreateAPIView):
    serializer_class = CarMilageSerializer


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



class TotalAPIView(APIView):
    """Задача Подключить drf-yasg. Настроить документацию для проекта. Создать эндпоинт на базе APIView для вывода

    общей информации по количеству машин, количеству мотоциклов, а также суммарному пробегу по машинам и мотоциклам.
    Описать для этого эндпоинта документацию вручную."""

    @swagger_auto_schema(responses={200: TotalDataSerializer})
    def get(self, *args, **kwargs):
        cars_milage = Milage.objects.filter(car__isnull=False).values_list('milage', flat=True)
        moto_milage = Milage.objects.filter(moto__isnull=False).values_list('milage', flat=True)
        response = {
            'total_cars': Car.objects.all().count(),
            'total_moto': Motorcycle.objects.all().count(),
            'total_cars_milage': sum(list(cars_milage)),
            'total_moto_milage': sum(list(moto_milage))
        }
        return Response(response)
