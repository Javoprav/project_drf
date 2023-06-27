from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=128, verbose_name='модель')
    year = models.PositiveSmallIntegerField(default=1900, verbose_name='год выпуска!')

    def __str__(self):
        return f'{self.model} ({self.year})'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Motorcycle(models.Model):
    model = models.CharField(max_length=128, verbose_name='модель')
    year = models.PositiveSmallIntegerField(default=1900, verbose_name='год выпуска!')

    def __str__(self):
        return f'{self.model} ({self.year})'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'
