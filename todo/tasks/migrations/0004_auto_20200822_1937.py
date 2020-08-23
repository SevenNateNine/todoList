# Generated by Django 3.1 on 2020-08-22 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200822_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 19, 37, 40, 396131), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 19, 37, 40, 396131), verbose_name='date updated'),
        ),
    ]
