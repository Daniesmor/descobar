# Generated by Django 2.1 on 2023-01-21 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_list', '0010_remove_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='day',
        ),
    ]
