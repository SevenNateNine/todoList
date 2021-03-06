# Generated by Django 3.1 on 2020-09-10 18:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_auto_20200910_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 10, 18, 28, 23, 417135), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 10, 18, 28, 23, 417135), verbose_name='date updated'),
        ),
    ]
