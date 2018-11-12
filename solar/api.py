from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from solar.models import TemperatureMeasurement

class TemperatureMeasurementResource(ModelResource):
    class Meta:
        queryset = TemperatureMeasurement.objects.all()
        resource_name = 'temperature-measurement'
        authorization = Authorization()
