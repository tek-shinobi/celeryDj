from celery import shared_task

from .services import add

@shared_task(name='sum two numbers')
def delayed_add(x, y):
    result = add(x,y)
    return result
