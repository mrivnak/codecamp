"""
To-Do list:
todo: verbose field names
todo: make sure on_delete is configured correctly for everything
"""
from django.db import models


class Venue(models.Model):
    VenueID = models.AutoField(primary_key=True),
    Venue_Name = models.CharField(max_length=50),  # todo: different max length? find way for no maximum?
    Address = models.CharField(max_length=50),


class Event(models.Model):
    EventID = models.AutoField(primary_key=True),
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE),
    start_datetime = models.DateField
    end_datetime = models.DateField


class Room(models.Model):
    RoomID = models.AutoField(primary_key=True),
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    # todo: room needs more data?


class Speaker(models.Model):
    SpeakerID = models.AutoField(primary_key=True),
    first_name = models.CharField(max_length=50),
    last_name = models.CharField(max_length=50),
    email = models.CharField(max_length=50),  # todo: verify valid email in backend before allowing addition. regex?
    phone_num = models.IntegerField


class Session(models.Model):
    SpeechID = models.AutoField(primary_key=True),
    Event = models.ForeignKey(Event, on_delete=models.CASCADE),
    Room = models.ForeignKey(Room, on_delete=models.CASCADE),
    start_datetime = models.DateField,
    end_datetime = models.DateField,
    Speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
