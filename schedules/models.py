from django.db import models
from datetime import datetime

# Create your models here.
class Schedules(models.Model):
    StartTime = models.DateTimeField(max_length=100)
    EndTime = models.DateTimeField(max_length=100)
    name = models.CharField(max_length=100)
    cell = models.CharField(max_length=100)
    LengthInMinutes = models.IntegerField(max_length=100)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return (
            self.name
            + " "
            + datetime.strftime(self.StartTime, "%x")
            + ", "
            + datetime.strftime(self.StartTime, "%X")
            + "  ->  "
            + datetime.strftime(self.EndTime, "%X")
            + ",       phone: "
            + self.cell
            + " ,     type: "
            + self.tag
        )
