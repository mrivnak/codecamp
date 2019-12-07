from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template import loader

from datetime import datetime, date

from .models import *
from .forms import *


def index(request):
    session_list = Session.objects.order_by()
    full_session_list = []
    template = loader.get_template('index.html')

    for session in session_list:
        sess = Session.objects.get(pk=session.pk)
        reports = sess.attendancereport_set.all()
        full_reports = []
        for i, report in enumerate(reports):
            full_reports.append({
                'report': report,
                'index': i+1,
            })

        full_session_list.append({
            'session': session,
            'reports': full_reports,
        })

    context = {
        'session_list': full_session_list
    }
    return HttpResponse(template.render(context, request))


def attendance(request, id):
    id = int(id)  # TODO: cast this better
    if request.method == 'POST':

        form = ReportForm(request.POST)

        if form.is_valid() or True:
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


def attendance_basic(request):

    if request.method == 'POST':

        form = ReportForm(request.POST)

        if form.is_valid():
            form.save()
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
    session_list = Session.objects.order_by()

    duration_list = []

    context = {
        'venue_list': venue_list,
        'event_list': event_list,
        'room_list': room_list,
        'speaker_list': speaker_list,
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
    instance = None
    if request.method == 'POST':

        if type == 'room':
            instance = Room.objects.get(pk=id)
            form = RoomForm(request.POST, instance=instance)
        elif type == 'speaker':
            instance = Speaker.objects.get(pk=id)
            form = SpeakerForm(request.POST, instance=instance)
        elif type == 'session':
            instance = Session.objects.get(pk=id)
            form = SessionForm(request.POST, instance=instance)
        elif type == 'venue':
            instance = Venue.objects.get(pk=id)
            form = VenueForm(request.POST, instance=instance)
        elif type == 'event':
            instance = Event.objects.get(pk=id)
            form = EventForm(request.POST, instance=instance)
        else:
            return HttpResponseNotFound("Invalid form option(s)")

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/')

    else:

        if type == 'room':
            instance = Room.objects.get(pk=id)
            form = RoomForm(instance=instance)
        elif type == 'speaker':
            instance = Speaker.objects.get(pk=id)
            form = SpeakerForm(instance=instance)
        elif type == 'session':
            instance = Session.objects.get(pk=id)
            form = SessionForm(instance=instance)
        elif type == 'venue':
            instance = Venue.objects.get(pk=id)
            form = VenueForm(instance=instance)
        elif type == 'event':
            instance = Event.objects.get(pk=id)
            form = EventForm(instance=instance)
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


def delete(request, type, id):
    instance = None
    if type == 'room':
        instance = Room.objects.get(pk=id)
        instance.delete()
    elif type == 'speaker':
        instance = Speaker.objects.get(pk=id)
        instance.delete()
    elif type == 'session':
        instance = Session.objects.get(pk=id)
        instance.delete()
    elif type == 'venue':
        instance = Venue.objects.get(pk=id)
        instance.delete()
    elif type == 'event':
        instance = Event.objects.get(pk=id)
        instance.delete()
    else:
        return HttpResponseNotFound("Invalid form option(s)")

    return HttpResponseRedirect('/admin/')


def data(request):
    report_list = AttendanceReport.objects.order_by()
    template = loader.get_template('data.html')

    context = {
        'report_list': report_list
    }
    return HttpResponse(template.render(context, request))


def data_user(request):
    report_list = AttendanceReport.objects.order_by()
    template = loader.get_template('data_user.html')

    context = {
        'report_list': report_list
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login.html')

    context = {
    }
    return HttpResponse(template.render(context, request))
