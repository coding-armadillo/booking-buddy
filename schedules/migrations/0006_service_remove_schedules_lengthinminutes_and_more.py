# Generated by Django 4.0.2 on 2022-03-12 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0004_remove_customer_appointments"),
        ("schedules", "0005_remove_schedules_cell_remove_schedules_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Service", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
                ("LengthInMinutes", models.IntegerField()),
                ("Charge", models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name="schedules",
            name="LengthInMinutes",
        ),
        migrations.RemoveField(
            model_name="schedules",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="schedules",
            name="tag",
        ),
        migrations.AddField(
            model_name="schedules",
            name="Customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="customers.customer",
            ),
        ),
        migrations.AddField(
            model_name="schedules",
            name="ServiceTable",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="schedules.service",
            ),
        ),
    ]
