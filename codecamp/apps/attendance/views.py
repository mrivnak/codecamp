from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template import loader

from datetime import datetime, date

from .models import Venue, Event, Room, Speaker, Timeslot, Session
from .forms import VenueForm, EventForm, RoomForm, TimeslotForm, SpeakerForm, SessionForm, ReportForm


def index(request):
    session_list = Session.objects.order_by()
    template = loader.get_template('index.html')

    context = {
        'session_list': session_list
    }
    return HttpResponse(template.render(context, request))


def attendance(request, id):
    id = int(id)  # TODO: cast this better
    if request.method == 'POST':

        form = ReportForm(request.POST)

        if form.is_valid() or True:  # TODO: figure out whi is_valid is always false
            question = form.save()
            question.Session = Session.objects.get(pk=id)
            question.save()
            return HttpResponseRedirect('/')

    else:
        form = ReportForm()

        template = loader.get_template('attendance.html')
        context = {
            'form': form,
        }
        return HttpResponse(template.render(context, request))


def admin(request):
    template = loader.get_template('admin.html')

    venue_list = Venue.objects.order_by()
    event_list = Event.objects.order_by()
    room_list = Room.objects.order_by()
    speaker_list = Speaker.objects.order_by()
    time_list = Timeslot.objects.order_by()
    session_list = Session.objects.order_by()

    duration_list = []

    for time in time_list:
        duration_list.append({'time': time,
                              'duration': int((datetime.combine(date.today(), time.end_time)
                                               - datetime.combine(date.today(), time.start_time)).seconds / 60)})

    context = {
        'venue_list': venue_list,
        'event_list': event_list,
        'room_list': room_list,
        'speaker_list': speaker_list,
        'time_list': time_list,
        'duration_list': duration_list,
        'session_list': session_list
    }
    return HttpResponse(template.render(context, request))


def form_add(request, type):

    if request.method == 'POST':

        if type == 'room':
            form = RoomForm(request.POST)
        elif type == 'speaker':
            form = SpeakerForm(request.POST)
        elif type == 'timeslot':
            form = TimeslotForm(request.POST)
        elif type == 'session':
            form = SessionForm(request.POST)
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
            form = RoomForm()
        elif type == 'speaker':
            form = SpeakerForm()
        elif type == 'timeslot':
            form = TimeslotForm()
        elif type == 'session':
            form = SessionForm()
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


def form_edit(request, type, id):
    pass


def delete(request, type, id):
    pass


def data(request):
    session_list = Session.objects.order_by()
    template = loader.get_template('data.html')

    context = {
        'session_list': session_list
    }
    return HttpResponse(template.render(context, request))