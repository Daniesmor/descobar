# Generated by Django 2.1 on 2022-12-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='university',
            field=models.CharField(max_length=100, null=True),
        ),
    ]