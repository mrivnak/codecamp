from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import loader

from datetime import datetime

from .models import Venue, Event, Room, Speaker, Timeslot, Session
from .forms import VenueForm, EventForm, SpeakerForm


def index(request):
    session_list = Session.objects.order_by()
    template = loader.get_template('index.html')

    context = {
        'session_list': session_list
    }
    return HttpResponse(template.render(context, request))


def attendance(request, id):
    session = Session.objects.get(pk=id)
    template = loader.get_template('attendance.html')
    context = {
        'id': id,
    }
    return HttpResponse(template.render(context, request))


def admin(request):
    venue_list = Venue.objects.order_by()
    event_list = Event.objects.order_by()
    room_list = Room.objects.order_by()
    speaker_list = Speaker.objects.order_by()
    time_list = Timeslot.objects.order_by()
    session_list = Session.objects.order_by()
    template = loader.get_template('admin.html')

    context = {
        'venue_list': venue_list,
        'event_list': event_list,
        'room_list': room_list,
        'speaker_list': speaker_list,
        'time_list': time_list,
        'session_list': session_list
    }
    return HttpResponse(template.render(context, request))


def form_add(request, type):

    if request.method == 'POST':

        if type == 'room':
            pass
        elif type == 'speaker':
            form = SpeakerForm(request.POST)
        elif type == 'timeslot':
            pass
        elif type == 'session':
            pass
        elif type == 'venue':
            form = VenueForm(request.POST)
        elif type == 'event':
            form = EventForm(request.POST)
        else:
            return HttpResponseNotFound("Invalid form option(s)")

        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/admin/')

    else:

        if type == 'room':
            pass
        elif type == 'speaker':
            form = SpeakerForm()
        elif type == 'timeslot':
            pass
        elif type == 'session':
            pass
        elif type == 'venue':
            form = VenueForm()
        elif type == 'event':
            form = EventForm()
        else:
            return HttpResponseNotFound("Invalid form option(s)")

        template = loader.get_template('form.html')
        context = {
            'form': form,
            'type': type,
            'action': 'add',
            'form_header': 'Add ' + type.capitalize(),
        }
        return HttpResponse(template.render(context, request))


def form_edit(request, type):
    pass
