from django.shortcuts import render, get_object_or_404, redirect
from daddle.models import Event, Pledge
from django.utils import timezone
from django.http import HttpResponseNotFound

import datetime

def index(request):
    start_date = timezone.now() - datetime.timedelta(hours=8)
    events = Event.objects.filter(start_date__gte=start_date).order_by('start_date')
    for event in events:
        event.current_user_has_active_pledge = event.user_has_active_pledge(request.user)
    context = {'events': events, 'user': request.user}
    return render(request, 'index.html', context)

def welcome(request):
    return render(request, 'welcome.html')

def pledge_user_to_event(request):
    event_id = request.POST["event-id"]
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    Pledge.objects.create(event=event, user=user, timestamp=timezone.now())

    return redirect('index')


def cancel_pledge(request):
    event_id = request.POST["event-id"]
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    pledge = _get_active_pledge(event, user)
    if not pledge:
        return HttpResponseNotFound("Pledge not found")

    pledge.cancel_timestamp=timezone.now()
    pledge.save()

    return redirect('index')


def single_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.current_user_has_active_pledge = event.user_has_active_pledge(request.user)

    context = {'event': event, 'user': request.user}
    return render(request, 'single_event.html', context)


def _get_active_pledge(event, user):
    for p in event.active_pledges():
        if p.user == user:
            return p

    return None

