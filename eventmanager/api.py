from tastypie.resources import ModelResource
from eventmanager.models import Event, Organization

import logging
import re

from datetime import date, datetime

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import simplejson

class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'

class OrganizationResource(ModelResource):
    class Meta:
        queryset = Organization.objects.all()
        resource_name = 'org'

def org_events(request, id=None):
    if (id != None):
        events = Event.objects.select_related().filter(org_id=id)
        json_result = {'events' : []}
        for item in events:
            event = {
                'event_name': item.event_name,
                'location': item.location,
                'start_date': item.start_date,
                'start_time': item.start_time,
                'end_date': item.end_date,
                'end_time': item.end_time,
            }
            json_result['events'].append(event)
        return HttpResponse(simplejson.dumps(json_result), mimetype='application/json')
