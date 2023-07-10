from django.db import models

# Create your models here.
class Languague(models.Model):
    languague = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
