from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    
    def __unicode__(self):
        return self.event_name
    
    # Returns list of all organizations.
    def getAllOrgs(self):
        return False;
        
    # Returns all events for specific organization.
    def getEvents(self):
        return False;

        
