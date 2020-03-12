from django.shortcuts import HttpResponse

from .tasks import add

def celery_view(request):
    for counter in range(2):
        task = add.delay(3, counter)
    return HttpResponse("FINISH PAGE LOAD")