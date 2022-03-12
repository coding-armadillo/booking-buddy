from django.db import models
from datetime import datetime
from customers.models import Customer

# Create your models here.
class Schedules(models.Model):
    StartTime = models.DateTimeField(max_length=100)
    EndTime = models.DateTimeField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    LengthInMinutes = models.IntegerField()
    tag = models.CharField(max_length=100)

    def __str__(self):
        if not self.customer:
            return (
                datetime.strftime(self.StartTime, "%x")
                + ", "
                + datetime.strftime(self.StartTime, "%X")
                + "  ->  "
                + datetime.strftime(self.EndTime, "%X")
                + " ,     type: "
                + self.tag
            )

        return (
            self.customer.first_name
            + " "
            + self.customer.last_name
            + " "
            + datetime.strftime(self.StartTime, "%x")
            + ", "
            + datetime.strftime(self.StartTime, "%X")
            + "  ->  "
            + datetime.strftime(self.EndTime, "%X")
            + ",       phone: "
            + self.customer.cell
            + " ,     type: "
            + self.tag
        )
