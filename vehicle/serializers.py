from rest_framework import serializers

from vehicle.models import Motorcycle, Car


class MotorcycleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Motorcycle
        fields = (
            'model',
            'year'
        )


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'model',
            'year'
        )
