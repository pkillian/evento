from tastypie.resources import ModelResource
from eventmanager.models import Event, Organization


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'

class OrganizationResource(ModelResource):
    class Meta:
        queryset = Organization.objects.all()
        resource_name = 'organization'

