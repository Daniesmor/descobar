from django.db import models
import datetime
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]


class Education(models.Model):
    studies = models.CharField(max_length=100)
    university = models.CharField(max_length=100, null=True)
    start = models.IntegerField(choices=YEAR_CHOICES, null=True)
    finish = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
