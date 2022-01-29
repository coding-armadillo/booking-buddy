from calendar import month_name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    current_time = datetime.now()
    context = {
        "now": make_aware(current_time)
    }
    return render(request, "schedules/index.html", context)

def about(request):
    return HttpResponse("this is not done go away")

def calender(request, month):
    current_month = datetime.now().month
    return HttpResponse(f"the month is {current_month} this also isn't done pls go away")