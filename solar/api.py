import datetime
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from solar.models import TemperatureMeasurement

class TemperatureMeasurementResource(ModelResource):
    class Meta:
        queryset = TemperatureMeasurement.objects.all()
        resource_name = 'temperature-measurement'
        authorization = Authorization()
        limit = 0
        filtering = {
            "measured_at": ['range'],
        }

class LastTemperatureMeasurementResource(ModelResource):
    class Meta:
        limit=1
        queryset = TemperatureMeasurement.objects.all().order_by('-measured_at')
        resource_name = 'last-temperature-measurement'
