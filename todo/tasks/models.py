from django.db import models
import datetime

class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200, blank=True, null=True)
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now())
    updated_date = models.DateTimeField('date updated', default=datetime.datetime.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title


