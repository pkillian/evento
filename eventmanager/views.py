import logging
import re
from eventmanager.models import EventForm

from django.http import HttpResponse, Http404, HttpResponseRedirect
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
from eventmanager.models import Event

def event_insert(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            EventForm.save()
        return HttpResponseRedirect('/thanks/')
    else:
        form = EventForm()
    
    return render(request, 'event_form.html', {
        'form': form,
    })