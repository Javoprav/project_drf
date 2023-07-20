from rest_framework import serializers
from vehicle.models import Motorcycle, Car, Milage
from vehicle.services import convert_currencies, convert_eur
from vehicle.validators import ModelValidator, validator_scam_words


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
    usd_price = serializers.SerializerMethodField()
    # вывод для запроса информации по машине список заполненных пробегов.
    eur_price = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_usd_price(self, instance):
        """Реализовать получение курса валют от сервиса currencyapi.com/ для вывода суммы машины или мотоцикла в
        долларах при условии, что изначально все суммы заводились в рублях."""
        return convert_currencies(instance.amount)

    def get_eur_price(self, instance):
        return convert_eur(instance.amount)

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
    model = serializers.CharField(max_length=128, validators=[validator_scam_words])
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


class TotalDataSerializer(serializers.Serializer):
    total_cars = serializers.IntegerField(default=0, label='Total car in storage')
    total_moto = serializers.IntegerField(default=0, label='Total moto in storage')
    total_cars_milage = serializers.IntegerField(default=0)
    total_moto_milage = serializers.IntegerField(default=0)
