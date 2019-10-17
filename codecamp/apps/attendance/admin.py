from django.contrib import admin
import codecamp.apps.attendance.models as models

# Register your models here.
# todo: add core functionality if we want it in default django-admin portal
for model in [models.Speaker, models.Room, models.Venue, models.Event, models.Session]:
    admin.site.register(model)
