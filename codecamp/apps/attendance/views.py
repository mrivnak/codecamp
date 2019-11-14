from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader

from datetime import datetime

from .models import Room, Speaker, Timeslot, Session


def index(request):
    session_list = Session.objects.order_by()
    template = loader.get_template('index.html')
    session_list = [
        {
            'title': 'Object Oriented Programming',
            'id': 0,
            'room': {
                'name': 'Room 1',
                'capacity': '500'
            },
            'speaker': {
                'name': 'John Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        },
        {
            'title': 'Artificial Intelligence with Python',
            'id': 2,
            'room': {
                'name': 'Room 2',
                'capacity': '300'
            },
            'speaker': {
                'name': 'Jason Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        },
        {
            'title': 'Object Oriented Programming',
            'id': 0,
            'room': {
                'name': 'Room 1',
                'capacity': '500'
            },
            'speaker': {
                'name': 'John Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        },
        {
            'title': 'Artificial Intelligence with Python',
            'id': 2,
            'room': {
                'name': 'Room 2',
                'capacity': '300'
            },
            'speaker': {
                'name': 'Jason Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        },
        {
            'title': 'Object Oriented Programming',
            'id': 0,
            'room': {
                'name': 'Room 1',
                'capacity': '500'
            },
            'speaker': {
                'name': 'John Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        },
        {
            'title': 'Artificial Intelligence with Python',
            'id': 2,
            'room': {
                'name': 'Room 2',
                'capacity': '300'
            },
            'speaker': {
                'name': 'Jason Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        },
    ]
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
    room_list = Room.objects.order_by()
    speaker_list = Speaker.objects.order_by()
    time_list = Timeslot.objects.order_by()
    session_list = Session.objects.order_by()
    template = loader.get_template('admin.html')
    room_list = [
        {
            'name': 'Room 1',
            'capacity': 500
        },
        {
            'name': 'Room 2',
            'capacity': 800
        }
    ]
    speaker_list = [
        {
            'name': 'John Smith',
            'email': 'john@gmail.com',
            'phone': '(123) 456-7890'
        },
        {
            'name': 'Jason Smith',
            'email': 'jason@gmail.com',
            'phone': '(098) 765-4321'
        }
    ]
    time_list = [
        {
            'start_time': datetime.now(),
            'end_time': datetime.now(),
            'duration': 60
        },
        {
            'start_time': datetime.now(),
            'end_time': datetime.now(),
            'duration': 120
        }
    ]
    session_list = [
        {
            'title': 'Object Oriented Programming',
            'room': {
                'name': 'Room 1',
                'capacity': '500'
            },
            'speaker': {
                'name': 'John Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        },
        {
            'title': 'Artificial Intelligence with Python',
            'room': {
                'name': 'Room 2',
                'capacity': '300'
            },
            'speaker': {
                'name': 'Jason Smith'
            },
            'timeslot': {
                'start_time': datetime.now(),
                'end_time': datetime.now()
            }
        }
    ]
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
