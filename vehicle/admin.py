from django.contrib import admin
from .models import *


@admin.register(Car)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'year', 'owner', 'amount',)
    list_filter = ('model',)


@admin.register(Motorcycle)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'owner',)
    list_filter = ('model', )


@admin.register(Milage)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('car', 'moto', 'year', 'milage',)
    list_filter = ('milage', )

