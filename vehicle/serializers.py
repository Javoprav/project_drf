from rest_framework import serializers
from vehicle.models import Motorcycle, Car, Milage
from vehicle.validators import ModelValidator


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


class CarMilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = ['year', 'milage', 'id']


class MotorcycleSerializers(serializers.ModelSerializer):
    # last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Motorcycle
        fields = '__all__'
        # fields = (
        #     'model',
        #     'year'
        # )

    # def get_last_milage(self, instance):
    #     milage = instance.milage_set.all().last()
    #     if milage:
    #         return milage.milage
    #     return 0


class CarSerializers(serializers.ModelSerializer):
    # last_milage = serializers.IntegerField(source='milage_set.last.milage', default=0, read_only=True)
    # добавление поля last_milage (последний пробег) только для чтения
    # last_milage = serializers.SerializerMethodField()

    milage = CarMilageSerializer(many=True, read_only=True, source='milage_set', required=False)

    # вывод для запроса информации по машине список заполненных пробегов.

    class Meta:
        model = Car
        fields = '__all__'

    # def create(self, validated_data):
    #     milage_data = validated_data.pop('milage_set')
    #     car_instance = Car.objects.create(**validated_data)
    #     for m in milage_data:
    #         Milage.objects.create(car=car_instance, **m)
    #     return car_instance

    # def get_last_milage(self, instance):
    #     milage = instance.milage_set.all().last()
    #     if milage:
    #         return milage.milage
    #     return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotorcycleSerializers(many=False)

    class Meta:
        model = Milage
        fields = ['year', 'milage', 'id', 'moto']
        # fields = '__all__'


class CarCreateSerializers(serializers.ModelSerializer):
    """Добавление пробега вместе с добавлением мотоцикла и машины."""

    milage = CarMilageSerializer(many=True, source='milage_set', required=False)

    class Meta:
        model = Car
        fields = '__all__'
        validators = [ModelValidator(field='model')]

    def create(self, validated_data):
        milage = None
        if 'milage_set' in validated_data:
            milage = validated_data.pop('milage_set')
        car_instance = Car.objects.create(**validated_data)
        if milage:
            for m in milage:
                Milage.objects.create(car=car_instance, **m)
        return car_instance
