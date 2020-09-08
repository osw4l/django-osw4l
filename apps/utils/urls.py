from django.urls import path
from django.conf.urls import url, include
from apps.niza.views import log_in


urlpatterns = [
    path('', log_in),
]
