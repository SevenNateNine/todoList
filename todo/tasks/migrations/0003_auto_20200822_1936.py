# Generated by Django 3.1 on 2020-08-22 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200822_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 19, 36, 23, 753367), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 19, 36, 23, 753367), verbose_name='date updated'),
        ),
    ]
