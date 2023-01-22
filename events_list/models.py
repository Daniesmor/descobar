from django.db import models


class Event(models.Model):
    MONTH_CHOICE = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    DAY_CHOICE = [(r, r) for r in range(1, 31 + 1)]

    event = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    day = models.IntegerField(choices=DAY_CHOICE)
    month = models.CharField(max_length=100, choices=MONTH_CHOICE)
    time = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=100, null=True, blank=True)
    info_url = models.CharField(max_length=100, null=True, blank=True)
