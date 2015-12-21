from django.template.loader import render_to_string
from django.db import models
from schedule.models import Event
 
def events(request):
    events = Event.objects.all()
    return render_to_string(['events.html'], {'events':events})
