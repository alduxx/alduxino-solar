from django.shortcuts import render
from django.http import HttpResponse

def main_panel(request):
    return render(request, 'alduxx/main_panel.html', {})
