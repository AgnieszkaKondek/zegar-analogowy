from django.urls import path
from .views import analog_clock

urlpatterns = [
    path('', analog_clock, name='analog_clock'),
]
