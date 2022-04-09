from calendar import month_name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from .models import Schedules
from calendar import calendar, setfirstweekday


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
    day = datetime.now().day
    dates = [
        [None, 1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12, 13],
        [14, 15, 16, 17, 18, 19, 20],
        [day - 6, day - 5, day - 4, day - 3, day - 2, day - 1, day],
        [day + 1, day + 2, day + 3, 31, None, None, None],
    ]

    calendar.setfirstweekday(6)
    c = calendar.month(2022, 3, w=2)

    month = datetime.now().month
    year = datetime.now().year

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

    context = {"schedules": schedules, "dates": dates, "month": month, "year": year}
    return render(request, "schedules/index.html", context)


def about(request):
    return HttpResponse("this is not done go away")


def calender(request, month):
    current_month = datetime.now().month
    return HttpResponse(
        f"the month is {current_month} this also isn't done pls go away"
    )
