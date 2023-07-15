from rest_framework import serializers
from vehicle.models import Motorcycle, Car


class ModelValidator:
    """Для эндпоинта создания машин и мотоциклов описать валидатор, который проверяет, что название модели состоит /
     только из букв, цифр и символов: точка, тире и пробел.
    Для создания эндпоинта создания машины и мотоцикла описать валидацию на проверку уникальности."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        model_name = value.get('model')
        if '#' in value.get('model'):
            raise serializers.ValidationError('Not acceptable character in model name')
        if Car.objects.filter(model=model_name).exists() \
                or Motorcycle.objects.filter(model=model_name).exists():
            raise serializers.ValidationError('Not unique model name')
