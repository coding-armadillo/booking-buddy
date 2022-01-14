from django.db import models
from django.http import HttpResponse
# Create your models here.



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")