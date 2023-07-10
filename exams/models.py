from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    exam_file = models.FileField(upload_to='exams/', max_length=254, **options)
    published = models.DateTimeField(default=now)
    num_exercise = models.IntegerField()

    def __str__(self):
        return self.title