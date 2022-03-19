from calendar import month_name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from .models import Schedules


def index(request):
    schedules = []
    for schedule in Schedules.objects.all():
        result = {
            "StartTime": schedule.StartTime,
            "EndTime": schedule.StartTime
            + timedelta(minutes=schedule.ServiceTable.LengthInMinutes),
            "Customer": schedule.Customer,
            "ServiceTable": schedule.ServiceTable,
        }
        schedules.append(result)

    context = {"schedules": schedules}
    return render(request, "schedules/index.html", context)


def about(request):
    return HttpResponse("this is not done go away")


def calender(request, month):
    current_month = datetime.now().month
    return HttpResponse(
        f"the month is {current_month} this also isn't done pls go away"
    )
