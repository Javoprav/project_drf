from celery import shared_task


@shared_task
def milage_check(milage_pk):
    print(f'we will work with milage pk: {milage_pk}')
