# Generated by Django 4.1.1 on 2022-10-16 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ourcalendar", "0002_events_origim"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="access",
            field=models.CharField(
                choices=[("PB", "Public"), ("PV", "Private")],
                default="PV",
                max_length=255,
            ),
            preserve_default=False,
        ),
    ]
