from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader

from .models import Room


def index(request):
    room_list = Room.objects.order_by()
    template = loader.get_template('index.html')
    context = {
        'room_list': room_list,
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
