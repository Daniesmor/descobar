from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToONeFIeld(User, on_delete=models.CASCADE)
    avatar = models.ImageFIeld(uplaod_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
