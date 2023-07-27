from celery import shared_task

from vehicle.models import Milage, Car


@shared_task
def milage_check(milage_pk):
    """Создать фоновую задачу, которая будет по изменению пробега у машины пересчитывать его суммарный пробег и
    выявлять несоответствия."""
    print(f'we will work with milage pk: {milage_pk}')
    milage_item = Milage.objects.filter(pk=milage_pk)
    if milage_item:
        biggest_milage = Milage.objects.filter(moto=milage_item.moto_id, milage__gt=milage_item.milage)
        if biggest_milage.exists():
            print('Not good owner')
            # send_mail
        else:
            print('Good owner')


def filter_check():
    """Создать задачу по расписанию, которая будет по заданным параметрам искать мотоциклы или машины и отправлять
    уведомление пользователю на почту."""
    filter_cond = {'price__lte': 100}
    cars_list = Car.objects.filter(**filter_cond)
    if cars_list.exists():
        print('send_mail')
