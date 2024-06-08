from django.shortcuts import render
import datetime
import pytz

def analog_clock(request):
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    tz = pytz.timezone('Europe/Warsaw')
    now = utc_now.astimezone(tz)

    hour_angle = (now.hour % 12) * 30 + (now.minute / 60) * 30 + 90  
    minute_angle = now.minute * 6 + 90  
    second_angle = now.second * 6+ 90

    context = {
        'hour_angle': hour_angle,
        'minute_angle': minute_angle,
        'second_angle': second_angle,
    }
    return render(request, 'clock/analog_clock.html', context)
