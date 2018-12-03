from django.utils.timezone import datetime #important if using timezones

from django.shortcuts import render
from solar.views import panel_by_date

def main_panel(request):
    today = datetime.today()
    return panel_by_date(request, today.year, today.month, today.day)
