from django.db import models
from django.conf import settings
import datetime

class Task(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200, blank=True, null=True)
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now())
    updated_date = models.DateTimeField('date updated', default=datetime.datetime.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title


