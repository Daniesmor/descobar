# Generated by Django 2.1 on 2023-01-20 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20230120_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 1, 20, 19, 3, 7, 90384), null=True),
        ),
    ]
