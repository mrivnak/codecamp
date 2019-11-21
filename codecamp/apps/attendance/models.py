"""
To-Do list:
todo: verbose field names
todo: make sure on_delete is configured correctly for everything
"""
from django.db import models


class Venue(models.Model):
    VenueID = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=50)  # todo: different max length? find way for no maximum?
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.venue_name


class Event(models.Model):
    EventID = models.AutoField(primary_key=True),
    event_name = models.CharField(max_length=50, name='event_name')
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.event_name


class Room(models.Model):
    RoomID = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    # todo: room needs more data?

    def __str__(self):
        return self.room_name


class Speaker(models.Model):
    SpeakerID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()  # todo: verify valid email in backend before allowing addition. regex?
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name + '' + self.last_name


class Session(models.Model):
    SessionID = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=50, name='session_name')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_name


class AttendanceReport(models.Model):
    ReportID = models.AutoField(primary_key=True)
    Session = models.ForeignKey(Session, on_delete=models.CASCADE)
    attendance = models.IntegerField()
    report_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.Session.session_name + ' - ' + self.report_time.strftime("%I:%m %p")
