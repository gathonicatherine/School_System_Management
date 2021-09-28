from django.db import models
from django.db.models.fields import CharField
 
class Event(models.Model):
   event_date=models.DateTimeField()
   event_agenda=models.CharField(max_length=20)
   event_duration=models.DateTimeField()
   event_planner_or_organiser=models.CharField(max_length=20, default='Samantha')
   event_venue=models.CharField(max_length=20, help_text=' Bool')
   number_of_attendees=models.PositiveSmallIntegerField(default=200)
   event_activity=CharField(max_length=20, default='Cultural day')
   signed_by=models.CharField(max_length=20, default='Samantha')
   start_time = models.DateTimeField(default='2021-07-04 00:00')
   end_time = models.DateTimeField(default='2021-07-04 00:00')
 
   def __str__(self):
       return self.event_activity