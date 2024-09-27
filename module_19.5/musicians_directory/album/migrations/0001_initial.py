# Generated by Django 5.0.7 on 2024-09-11 09:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("musician", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="album_model",
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
                ("Album_Name", models.CharField(max_length=75)),
                (
                    "Album_Release_Date",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 9, 11, 9, 20, 20, 207527)
                    ),
                ),
                (
                    "Rating",
                    models.IntegerField(
                        choices=[
                            (1, "1 - Very Bad"),
                            (2, "2 - Bad"),
                            (3, "3 - Average"),
                            (4, "4 - Good"),
                            (5, "5 - Excellent"),
                        ]
                    ),
                ),
                (
                    "Musician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="musician.musician_model",
                    ),
                ),
            ],
        ),
    ]
