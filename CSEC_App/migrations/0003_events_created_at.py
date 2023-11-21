# Generated by Django 4.2.7 on 2023-11-21 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("CSEC_App", "0002_events"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]