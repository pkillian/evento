from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

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
from django.views.decorators.csrf import csrf_exempt

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
        org_name = None
        for item in Organization.objects.select_related().filter(id=org_id):
            org_name = item.org_name
            break

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

@csrf_exempt
def analytic_store(request):
    data=simplejson.loads(request.raw_post_data)
    for item in data:
        event_analytic = EventAnalytic()
        value = item['event_name']
        event_analytic.event_name = value
        event_analytic.event_time = datetime.datetime.now()
        event_analytic.save()
    response = HttpResponse("OK")
    response.status_code = 200
    return response

