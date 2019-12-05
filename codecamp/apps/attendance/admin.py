from django.contrib import admin
from .models import *

# Register your models here.
# todo: add core functionality if we want it in default django-admin portal
admin.site.register(Speaker)
admin.site.register(Room)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Timeslot)
admin.site.register(Session)
admin.site.register(AttendanceReport)
