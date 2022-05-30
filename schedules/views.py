from calendar import month_name
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from .models import Schedules
import calendar


def index(request):
    now = datetime.now()
    return redirect("schedules:calendar", now.year, now.month)


def about(request):
    return HttpResponse("this is not done go away")


def get_calendar(request, year, month):

    schedules = []
    for schedule in Schedules.objects.filter(
        StartTime__month=month, StartTime__year=year
    ):

        result = {
            "StartTime": schedule.StartTime,
            "EndTime": schedule.StartTime
            + timedelta(minutes=schedule.ServiceTable.LengthInMinutes),
            "Customer": schedule.Customer,
            "ServiceTable": schedule.ServiceTable,
        }
        schedules.append(result)
    dates = []

    calendar.setfirstweekday(6)
    calen = calendar.month(year, month, w=2)
    lines = calen.strip().split("\n")[2:]
    calen = 0
    for line in lines:
        days = line.split()
        if calen == 0 and len(days) < 7:
            days = [None] * (7 - len(days)) + days
        dates.append(days)
        calen += 1

    next_year = year
    prev_year = year
    next_month = month + 1
    if next_month > 12:
        next_month = 1
        next_year = next_year + 1
    prev_month = month - 1
    if prev_month < 1:
        prev_month = 12
        prev_year = prev_year - 1

    if month == 1:
        month = "January"
    elif month == 2:
        month = "Feburary"
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
        "next_month": next_month,
        "prev_month": prev_month,
        "next_year": next_year,
        "prev_year": prev_year,
    }
    return render(request, "schedules/index.html", context)
