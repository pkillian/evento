from django.db import models
from django.forms import ModelForm

# Create your models here.
class Organization(models.Model):
    org_name = models.CharField(max_length=100)
        
    def __unicode__(self):
        return self.org_name
    
class OrgForm(ModelForm):
    class Meta:
        model = Organization

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    org_id = models.ForeignKey(Organization)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    
    def __unicode__(self):
        return self.event_name

class EventForm(ModelForm):
    class Meta:
        model = Event
    
class EventAnalytic(models.Model):
    event_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.IntegerField()

    def __unicode__(self):
        return self.event_id
