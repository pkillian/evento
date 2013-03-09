from django.conf.urls.defaults import patterns, include, url
from eventmanager.api import EventResource, OrganizationResource
from eventmanager import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

org_handle = OrganizationResource();
event_handle = EventResource();

#handler500 = 'eventmanager.views.custom_500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evento.views.home', name='home'),
    # url(r'^evento/', include('evento.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/org_events/(?P<id>\d+)$', 'eventmanager.api.org_events', name='Org_Events'),

    url(r'^api/analytics/$', 'eventmanager.api.analytic_store', name='Analytic_Store'),

    url(r'^api/', include(event_handle.urls)),
    url(r'^api/', include(org_handle.urls)),
    
    url(r'^org-form/$', views.org_insert),
    url(r'^event-form/$', views.event_insert),
    url(r'^event-form-fucked/$', views.event_insert_fucked),
    url(r'^thanks/$', views.thank_you),
    url(r'^orgs/$', views.view_orgs),
    url(r'^data/$', views.view_data),
    url(r'^$', views.homepage)
)
