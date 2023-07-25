from celery import shared_task

from vehicle.models import Milage


@shared_task
def milage_check(milage_pk):
    print(f'we will work with milage pk: {milage_pk}')
    milage_item = Milage.objects.filter(pk=milage_pk)
    if milage_item:
        biggest_milage = Milage.objects.filter(moto=milage_item.moto, milage__gt=milage_item.milage)
        if biggest_milage.exists():
            print('Not good owner')
            # send_mail
        else:
            print('Good owner')
