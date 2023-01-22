from django.shortcuts import render
from .models import Event


def events_list(request):
    events = Event.objects.all()
    return render(request, "events_list/events_list.html", {'events_list': events})
