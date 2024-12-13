# Generated by Django 4.2 on 2024-06-27 14:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("appointments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medication",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("manufacturer", models.CharField(max_length=100)),
                ("milligrams", models.IntegerField()),
                ("precautions", models.TextField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Prescription",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("prescription", models.TextField()),
                ("instructions", models.TextField()),
                ("issued_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "appointment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appointments.appointment",
                    ),
                ),
                ("medications", models.ManyToManyField(to="prescriptions.medication")),
            ],
        ),
    ]