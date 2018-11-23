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

    #def get_object_list(self, request):
    #    return super(TemperatureMeasurementResource, self).get_object_list(request).filter(measured_at__contains=datetime.date(2018, 11, 14))

#measured_at__range=2018-11-14T00:00,2018-11-14T23:55
