# Generated by Django 4.0.2 on 2022-04-30 22:08

from unicodedata import name
from django.db import migrations


def add_rows(apps, scema_editor):
    Service = apps.get_model("schedules", "Service")
    services = [
        ("Men Haircut", "Haircut", 20, 15),
        ("Men Wash+Haircut+style", "Haircut", 30, 18),
        ("Woman Haircut", "Haircut", 30, 22),
        ("Woman Wash+Haircut+style", "Haircut", 45, 28),
        ("Boy Haircut", "Haircut", 20, 12),
        ("Girl Haircut", "Haircut", 30, 15),
        ("wash and style (short)", "style", 30, 15),
        ("wash and style(long)", "style", 40, 25),
        ("Men Color + Cut(10min color)", "Color/Haircut", 60, 40),
        ("Men Color + Cut(45min color)", "Color/Haircut", 90, 60),
        ("Root Retouch(short)", "Color", 90, 50),
        ("Root Retouch(long)", "Color", 90, 60),
        ("Color + Highlight+cut(short)", "Color/Haircut", 150, 110),
        ("Color + Highlight+cut(long)", "Color/Haircut", 180, 155),
        ("Full Head Highlight", "Color", 150, 100),
        ("Partial Highlight", "Color", 90, 65),
        ("Full Head Color(short)", "Color", 90, 600),
        ("Full Head Color(long)", "Color", 120, 70),
        ("Balayage&ombre", "Color", 210, 150),
        ("Straightening+(cut)", "Straightening", 210, 150),
        ("Perm(short)", "Perm", 120, 65),
        ("Perm(long)", "Perm", 180, 75),
        ("Massage(30 minutes)", "Massage", 60, 80),
        ("Massage(1 hour)", "Massage", 30, 40),
        ("Massage(90 minutes)", "Massage", 90, 120),
        ("Massage(15 minutes)", "Massage", 15, 20),
        ("Massage(2 hour)", "Massage", 120, 160),
    ]
    for name, type_name, duration, cost in services:
        s = Service(
            Service=name,
            type=type_name,
            LengthInMinutes=duration,
            Charge=cost,
        )
        s.save()


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0007_remove_schedules_endtime"),
    ]

    operations = [migrations.RunPython(add_rows)]
