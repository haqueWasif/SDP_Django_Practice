# Generated by Django 5.0.7 on 2024-09-22 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("album", "0002_alter_album_model_album_release_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album_model",
            name="Album_Release_Date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 9, 22, 9, 19, 2, 275651, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
