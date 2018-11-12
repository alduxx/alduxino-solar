from django.urls import path, include
from solar.api import TemperatureMeasurementResource
from . import views

temperature_measurement_resource = TemperatureMeasurementResource()

urlpatterns = [
    path('', views.index, name='index'),
    #path('/api/solar-heating/temperature-measurements/', views.api_sh_tm, name='api_sh_tm'),
    path('api/', include(temperature_measurement_resource.urls)),
]
