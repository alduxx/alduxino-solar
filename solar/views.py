import datetime
from django.shortcuts import render
from django.http import HttpResponse
from solar.models import TemperatureMeasurement

def index(request):
    return HttpResponse("Solar Heating Main Panel.")

def panel_by_date(request, year, month, day):
    current_date = datetime.date(year, month, day)
    start_time = "%d-%d-%dT00:00" % (year, month, day)
    end_time = "%d-%d-%dT23:59" % (year, month, day)

    zero_hour = datetime.datetime(current_date.year, current_date.month, current_date.day, 0, 0)
    midnight = datetime.datetime(current_date.year, current_date.month, current_date.day, 23, 59)

    last_reading = TemperatureMeasurement.objects.filter(measured_at__range=(zero_hour, midnight)).last()

    return render(request, 'alduxx/solar_main_panel.html', {
        'current_date': current_date,
        'start_time': start_time,
        'end_time': end_time,
        'last_reading': last_reading
    })
