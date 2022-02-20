from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime
from django.utils.timezone import make_aware
from .models import Customer


def index(request):

    context = {"customers": Customer.objects.all()}
    return render(request, "customers/index.html", context)


def about(request):
    return HttpResponse("Hello to the about page")


def detail(request, customer_id):
    return HttpResponse(f"hello, customer with id: {customer_id}")
