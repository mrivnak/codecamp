from django import forms
from codecamp.apps.attendance.models import Speaker, Room, Timeslot, Session, Venue, Event


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_name', 'address']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'Venue', 'start_date', 'end_date', 'start_time', 'end_time']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'capacity', 'Venue']


class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ['date', 'start_time', 'end_time']


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['first_name', 'last_name', 'email', 'phone_num']


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session_name', 'Event', 'Room', 'Timeslot', 'Speaker']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['attendance']
