from django.urls import path, include
from solar.api import TemperatureMeasurementResource, LastTemperatureMeasurementResource
from . import views

temperature_measurement_resource = TemperatureMeasurementResource()
last_temperature_measurement_resource = LastTemperatureMeasurementResource()

urlpatterns = [
    path('', views.index, name='index'),
    path('on/<int:year>/<int:month>/<int:day>''', views.panel_by_date, name='panel_by_date'),
    #path('/api/solar-heating/temperature-measurements/', views.api_sh_tm, name='api_sh_tm'),
    path('api/', include(temperature_measurement_resource.urls)),
    path('api/', include(last_temperature_measurement_resource.urls)),
]
