import logging
import re
import sys
from eventmanager.models import EventForm, OrgForm, Organization, Event


from django.template import Context
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseServerError
from django.conf import settings
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils import simplejson
from django.db import transaction
from django.views.generic.edit import FormView

from datetime import date, time, timedelta

def event_insert(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = EventForm()
    
    return render(request, 'event_form.html', {
        'form': form,
    })

def event_insert_style(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = EventForm()
    
    return render(request, 'event_form_twitter.html', {
        'form': form,
    })

def org_insert(request):
    if request.method == 'POST':
        form = OrgForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/event-form/')
    else:
        form = OrgForm()
    
    return render(request, 'org_form.html', {
        'form': form,
    })

def org_insert_style(request):
    if request.method == 'POST':
        form = OrgForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/event-form/')
    else:
        form = OrgForm()
    
    return render(request, 'org_form_twitter.html', {
        'form': form,
    })

def thank_you(request):
    return render(request, 'thank_you.html')

def homepage(request):
    return render(request, 'homepage.html')

def view_orgs(request):
    listoforgs = Organization.objects.all()

    return render(request, 'orglist.html', {'listoforgs':listoforgs})

def view_data(request):
    allData = Event.objects.all()
    
    return render(request, 'data.html', {'allData':allData})

        
    
    

