# Generated by Django 2.2.5 on 2019-11-21 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('RoomID', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('SpeakerID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('VenueID', models.AutoField(primary_key=True, serialize=False)),
                ('venue_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('SessionID', models.AutoField(primary_key=True, serialize=False)),
                ('session_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Event')),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Room')),
                ('Speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Speaker')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='Venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Venue'),
        ),
        migrations.AddField(
            model_name='event',
            name='Venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Venue'),
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('ReportID', models.AutoField(primary_key=True, serialize=False)),
                ('attendance', models.IntegerField()),
                ('report_time', models.TimeField(auto_now=True)),
                ('Session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Session')),
            ],
        ),
    ]
