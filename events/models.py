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
    #day = models.CharField(max_length=100, choices=DAY_CHOICE, null=True, blank=True)
    day = models.IntegerField()
    month = models.CharField(max_length=100, choices=MONTH_CHOICE, null=True, blank=True)
    #time = models.DateTimeField(null=True, blank=True)
