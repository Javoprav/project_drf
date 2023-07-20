from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import RegexValidator

NULLABLE = {'null': True, 'blank': True}


class Car(models.Model):
    model = models.CharField(max_length=128, verbose_name='модель')  # validators=[RegexValidator] - Встроенный валидатор
    year = models.PositiveSmallIntegerField(default=1900, verbose_name='год выпуска!')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    amount = models.IntegerField(default=1000, verbose_name='цена')

    def __str__(self):
        return f'{self.model} ({self.year})'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Motorcycle(models.Model):
    model = models.CharField(max_length=128, verbose_name='модель')
    year = models.PositiveSmallIntegerField(default=1900, verbose_name='год выпуска!')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.model} ({self.year})'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, **NULLABLE, related_name='milage')
    moto = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, **NULLABLE)

    year = models.PositiveSmallIntegerField(default=0, verbose_name='год регистрации пробега')
    milage = models.PositiveSmallIntegerField(default=0, verbose_name='пробег')

    def __str__(self):
        return f'{self.car if self.car else self.moto} - {self.milage} ({self.year}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('year',)
