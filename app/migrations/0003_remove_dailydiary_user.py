# Generated by Django 4.1.2 on 2024-04-03 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_dailydiary"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dailydiary",
            name="user",
        ),
    ]
