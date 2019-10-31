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
