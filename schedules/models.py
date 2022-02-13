from django.db import models
from datetime import datetime

# Create your models here.
class Schedules(models.Model):
    appointment_dayandtime = models.DateTimeField(max_length=100)
    name = models.CharField(max_length=100)
    cell = models.CharField(max_length=100)

    def __str__(self):
        return self.name + datetime.strftime(self.appointment_dayandtime, "%c")
