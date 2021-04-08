from django.db import models
from django.conf import settings
from django.utils import timezone


class Priority(models.Model):
    description = models.CharField(max_length=30, default='')
    order = models.IntegerField()

    def __str__(self):
        return self.description


class Todo(models.Model):
    description = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description
