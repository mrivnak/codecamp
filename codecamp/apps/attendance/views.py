from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader

from .models import Room, Speaker, Timeslot, Session


def admin(request):
    room_list = Room.objects.order_by()
    speaker_list = Speaker.objects.order_by()
    time_list = Timeslot.objects.order_by()
    session_list = Session.objects.order_by()
    template = loader.get_template('admin.html')
    context = {
        'room_list': room_list,
        'speaker_list': speaker_list,
        'time_list': time_list,
        'session_list': session_list
    }
    return HttpResponse(template.render(context, request))


def form(request, type, action):
    types = {'room', 'speaker','timeslot', 'session'}
    actions = {'add', 'edit'}
    if type in types and action in actions:
        template = loader.get_template('form.html')
        context = {
            'type': type,
            'action': action,
            'form_header': action.capitalize() + ' ' + type.capitalize(),
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseNotFound("Invalid form option(s)")
