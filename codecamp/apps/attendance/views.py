from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VenueSerializer
from .models import Venue, Event, Room, Speaker, Session


# Create your views here.
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all().order_by('room')
    serializer_class = VenueSerializer
