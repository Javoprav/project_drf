import datetime

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


@shared_task
def send_message_about_like():
    print(f"Сообщение отправлено в чат тг")


def send_today_milage_mail():
    """Для работы с очередями реализовать функционал лайков и отправлять пользователю письмо на электронную почту.
    Для работы с периодическими задачами добавить поле «Дата рождения собаки» и отправлять хозяину поздравление с
    днем рождения на электронную почту. Для обеих рассылок реализовать отправку через телеграм-бота."""
    milage_list = Milage.objects.filter(year=datetime.date.today())
    for item in milage_list:
        print(f"Send mail for user in {item}")