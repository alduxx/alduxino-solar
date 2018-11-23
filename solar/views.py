import datetime
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Solar Heating Main Panel.")

def panel_by_date(request, year, month, day):
    current_date = datetime.date(year, month, day)
    start_time = "%d-%d-%dT00:00" % (year, month, day)
    end_time = "%d-%d-%dT23:59" % (year, month, day)

    return render(request, 'alduxx/main_panel.html', {
        'current_date': current_date,
        'start_time': start_time,
        'end_time': end_time
    })
