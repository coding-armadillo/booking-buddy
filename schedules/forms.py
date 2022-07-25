from django import forms
from django.forms import ModelForm
from schedules.models import Schedules
from django import forms

time_choices = [(d, f"{str(d).zfill(2)}:00") for d in range(9, 21)]


class AppointmentForm(ModelForm):
    date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-200 appearance-none border-2 border-gray-200 rounded-lg w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-blue-500",
                "x-model": "event_date",
                "readonly": True,
            }
        )
    )
    time = forms.IntegerField(widget=forms.Select(choices=time_choices))

    class Meta:
        model = Schedules
        fields = ["Customer", "ServiceTable"]
