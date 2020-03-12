from django.shortcuts import HttpResponse

from .tasks import delayed_add

def celery_view(request):
    for counter in range(2):
        delayed_add.delay(3, counter)
    return HttpResponse("FINISH PAGE LOAD")