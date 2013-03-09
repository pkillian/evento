from tastypie.resources import ModelResource
from eventmanager.models import Event, Organization, EventAnalytic

import logging
import re

import time
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

        org_id = id
        org_name = Organization.objects.select_related().filter(id=org_id)[0].org_name

        json_result['org_id'] = int(org_id)
        json_result['org_name'] = org_name

        for item in events:
            event = {
                'event_name': item.event_name,
                'location': item.location,
                'start': time.mktime(datetime.combine(item.start_date, item.start_time).timetuple()),
                'end': time.mktime(datetime.combine(item.end_date, item.end_time).timetuple()),
            }
            json_result['events'].append(event)
        return HttpResponse(simplejson.dumps(json_result), mimetype='application/json')

def analytic_store(request):
    for item in request.POST['analytics']
        event_analytic = EventAnalytic()
        event_analytic.event_id = int(item['event_id'])
        event_analytic.latitude = int(item['latitude'])
        event_analytic.longitude = int(item['longitude'])
        event_analytic.date = int(item['date'])
