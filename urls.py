from django.conf.urls.defaults import patterns, include, url
from eventmanager.api import EventResource, OrganizationResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

org_handle = OrganizationResource();
event_handle = EventResource();

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evento.views.home', name='home'),
    # url(r'^evento/', include('evento.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(event_handle.urls)),
)
