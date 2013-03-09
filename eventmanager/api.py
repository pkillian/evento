from tastypie.resources import ModelResource
from eventmanager.models import Entry, Organization


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'

class OrganizationResource(ModelResource):
    class Meta:
        queryset = Organization.objects.all()
        resource_name = 'organization'

