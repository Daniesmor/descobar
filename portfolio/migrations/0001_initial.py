# Generated by Django 2.1 on 2022-12-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('studies', models.CharField(max_length=100)),
            ],
        ),
    ]
