"""
TODO:
 - Implement this module properly
"""
from rest_framework import serializers
from .models import Venue, Event, Room, Speaker, Session


# just an example so we can go more in depth later
class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = ('VenueID', 'Venue_Name', 'Address')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('EventID', 'Venue', 'start_datetime', 'end_datetime')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('RoomID', 'Venue')

class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        fields = ('SpeakerID', 'first_Name', 'last_name', 'email', 'phone_num')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('SpeechID', 'Event', 'Room', 'start_datetime', 'end_datetime', 'Speaker')
