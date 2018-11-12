from django.contrib import admin
from django.urls import include, path

from alduxx import views

urlpatterns = [
    path('', views.main_panel, name='main_panel'),
    path('solar/', include('solar.urls')),
]
