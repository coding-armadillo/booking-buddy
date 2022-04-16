from calendar import month_name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from .models import Schedules
import calendar


def index(request):
    now = datetime.now()
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
    day = now.day
    dates = []

    calendar.setfirstweekday(6)
    calen = calendar.month(now.year, now.month, w=2)
    lines = calen.strip().split("\n")[2:]
    calen = 0
    for line in lines:
        days = line.split()
        if calen == 0 and len(days) < 7:
            days = [None] * (7 - len(days)) + days
        dates.append(days)
        calen += 1

    month = now.month
    year = now.year
    date = now.day

    if month == 1:
        month = "January"
    elif month == 2:
        month = "Febuary"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    elif month == 12:
        month = "December"

    context = {
        "schedules": schedules,
        "dates": dates,
        "month": month,
        "year": year,
        "date": day,
    }
    return render(request, "schedules/index.html", context)


def about(request):
    return HttpResponse("this is not done go away")


def calender(request, month):
    now = datetime.now()
    current_month = now.month
    return HttpResponse(
        f"the month is {current_month} this also isn't done pls go away"
    )
