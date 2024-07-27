# accounts/models.py
from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=200, default='Default Event Name')
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
