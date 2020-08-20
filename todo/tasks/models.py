from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    updated_date = models.DateTimeField('date updated')
    completed = models.BooleanField()

    def __str__(self):
        return self.task_text


