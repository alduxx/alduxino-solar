from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from alduxx import views

urlpatterns = [
    path('', views.main_panel, name='main_panel'),
    path('solar/', include('solar.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
