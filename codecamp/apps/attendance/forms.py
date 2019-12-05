from django import forms

from codecamp.apps.attendance.models import *


class VenueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VenueForm, self).__init__(*args, **kwargs)
        self.fields['venue_name'].widget.attrs = {'class': 'form-control'}
        self.fields['address'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Venue
        fields = ['venue_name', 'address']


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['event_name'].widget.attrs = {'class': 'form-control'}
        self.fields['Venue'].widget.attrs = {'class': 'form-control'}

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
            }
        )
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Event
        fields = ['event_name', 'Venue', 'start_date', 'end_date', 'start_time', 'end_time']


class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['room_name'].widget.attrs = {'class': 'form-control'}
        self.fields['capacity'].widget.attrs = {'class': 'form-control'}
        self.fields['Venue'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Room
        fields = ['room_name', 'capacity', 'Venue']


class SpeakerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SpeakerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {'class': 'form-control'}
        self.fields['last_name'].widget.attrs = {'class': 'form-control'}

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'tel',
                'class': 'form-control',
                'pattern': '[0-9]{10-13}',
            }
        )
    )

    def clean_phone_num(self):
        phone_num = self.cleaned_data['phone_number']
        for char in phone_num:
            if char not in range(9):
                phone_num.remove(char)
        return phone_num

    class Meta:
        model = Speaker
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class SessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)
        self.fields['session_name'].widget.attrs = {'class': 'form-control'}
        self.fields['Event'].widget.attrs = {'class': 'form-control'}
        self.fields['Room'].widget.attrs = {'class': 'form-control'}
        self.fields['Speaker'].widget.attrs = {'class': 'form-control'}

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
            }
        )
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Session
        fields = ['session_name', 'date', 'start_time', 'end_time', 'Event', 'Room', 'Speaker']


class ReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['Session'].widget.attrs = {'class': 'form-control'}
        self.fields['attendance'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = AttendanceReport
        fields = ['Session', 'attendance']
