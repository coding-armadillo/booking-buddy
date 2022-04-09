from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime
from django.utils.timezone import make_aware
from .models import Customer
from schedules.models import Schedules


def index(request):
    customers = []
    for customer in Customer.objects.all():
        result = {
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "cell": customer.cell,
            "email": customer.email,
            "number_of_appointments": 0,
        }
        result["number_of_appointments"] = Schedules.objects.filter(
            Customer=customer
        ).count()

        result["next_appointment"] = (
            Schedules.objects.filter(Customer=customer, StartTime__gt=datetime.now())
            .order_by("StartTime")
            .first()
        )

        customers.append(result)
        context = {"customers": customers}
        return render(request, "customers/index.html", context)


def about(request):
    return HttpResponse("Hello to the about page")


def detail(request, customer_id):
    return HttpResponse(f"hello, customer with id: {customer_id}")
