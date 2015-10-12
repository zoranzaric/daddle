from django.shortcuts import render
from daddle.models import Event

import datetime

def index(request):
    events = Event.objects.filter(start_date__gte=datetime.datetime.now())
    context = {'events': events}
    return render(request, 'index.html', context)
