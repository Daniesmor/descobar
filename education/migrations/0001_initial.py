# Generated by Django 2.1 on 2023-01-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studies', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100, null=True)),
                ('start', models.DateField(null=True)),
                ('finish', models.DateField(null=True)),
            ],
        ),
    ]
