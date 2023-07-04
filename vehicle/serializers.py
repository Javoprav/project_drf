from rest_framework import serializers

from vehicle.models import Motorcycle, Car, Milage


class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = '__all__'


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
    last_milage = serializers.IntegerField(source='milage_set.last.milage', default=0, read_only=True)
    # добавление поля last_milage (последний пробег) только для чтения
    # last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Car
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