import logging
import re

from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils import simplejson
from django.db import transaction

from datetime import date, time, timedelta
