from django.db import models


# Create your models here.
class Link(models.Model):
    key_icon = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)