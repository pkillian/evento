from django import forms
from django.db import models
from django.forms import ModelForm
from bootstrap_toolkit.widgets import BootstrapTextInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

# Create your models here.
class Organization(models.Model):
    org_name = models.CharField(max_length=100)
        
    def __unicode__(self):
        return self.org_name
    
class OrgForm(ModelForm):  
    
    class Meta:
        model = Organization
        fields = ('org_name',)
        widgets = {
            'org_name': BootstrapTextInput()
        }


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
    
    def __init__(self, *args, **kwargs):
        
        self.helper = FormHelper() 
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        
        self.helper.add_input(Submit('submit', 'Submit'))

        
        super(EventForm, self).__init__(*args, **kwargs)


        
    class Meta:
        model = Event
    
class EventAnalytic(models.Model):
    event_name = models.CharField(max_length=100)
    event_time = models.TimeField()

    def __unicode__(self):
        return self.event_name
