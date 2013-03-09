from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.event_name

class Organization(models.Model):
    org_name = models.CharField(max_length=100)
        
    def __unicode__(self):
        return self.org_name
    



        
