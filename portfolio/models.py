from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to="portfolio", null=True, blank=True)
    studies = models.CharField(max_length=100)
    university = models.CharField(max_length=100, null=True)
