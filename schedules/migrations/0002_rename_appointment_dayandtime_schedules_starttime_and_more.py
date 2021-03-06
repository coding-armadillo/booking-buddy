# Generated by Django 4.0.1 on 2022-02-20 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("schedules", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="schedules",
            old_name="appointment_dayandtime",
            new_name="StartTime",
        ),
        migrations.AddField(
            model_name="schedules",
            name="EndTime",
            field=models.DateTimeField(
                default=django.utils.timezone.now, max_length=100
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="schedules",
            name="length",
            field=models.IntegerField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="schedules",
            name="tag",
            field=models.CharField(default="haircut", max_length=100),
            preserve_default=False,
        ),
    ]
