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

    def __str__(self):
        return self.Venue_Name


class Event(models.Model):
    EventID = models.AutoField(primary_key=True),
    event_name = models.CharField(max_length=50, name='event_name')
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE),
    start_datetime = models.DateField
    end_datetime = models.DateField

    def __str__(self):
        return self.event_name


class Room(models.Model):
    RoomID = models.AutoField(primary_key=True),
    name = models.CharField(max_length=50),
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    # todo: room needs more data?

    def __str__(self):
        return self.room_name


class Timeslot(models.Model):
    TimeslotID = models.AutoField(primary_key=True),
    start_datetime = models.DateTimeField,
    end_datetime = models.DateTimeField


class Speaker(models.Model):
    SpeakerID = models.AutoField(primary_key=True),
    first_name = models.CharField(max_length=50),
    last_name = models.CharField(max_length=50),
    email = models.CharField(max_length=50),  # todo: verify valid email in backend before allowing addition. regex?
    phone_num = models.IntegerField

    def __str__(self):
        return self.first_name+self.last_name


class Session(models.Model):
    SpeechID = models.AutoField(primary_key=True),
    session_name = models.CharField(max_length=50, name='session_name')
    Event = models.ForeignKey(Event, on_delete=models.CASCADE),
    Room = models.ForeignKey(Room, on_delete=models.CASCADE),
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE),
    Speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_name